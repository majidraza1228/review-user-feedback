import sqlite3
import json
from flask import Flask, render_template, request, jsonify, g
from datetime import datetime

app = Flask(__name__)
DATABASE = 'database.db'


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row
    return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()


@app.route('/')
def index():
    db = get_db()
    products = db.execute('''
        SELECT
            p.id,
            p.name,
            p.category,
            p.description,
            ROUND(AVG(f.rating), 1) as avg_rating,
            COUNT(f.id) as review_count
        FROM products p
        LEFT JOIN feedback f ON p.id = f.product_id
        GROUP BY p.id
        ORDER BY p.name
    ''').fetchall()
    return render_template('index.html', products=products)


@app.route('/product/<int:product_id>')
def product(product_id):
    db = get_db()
    product = db.execute(
        'SELECT * FROM products WHERE id = ?', (product_id,)
    ).fetchone()

    if product is None:
        return render_template('404.html'), 404

    reviews = db.execute('''
        SELECT rating, comment, reviewer_name, created_at
        FROM feedback
        WHERE product_id = ?
        ORDER BY created_at DESC
    ''', (product_id,)).fetchall()

    avg_rating = db.execute(
        'SELECT ROUND(AVG(rating), 1) as avg FROM feedback WHERE product_id = ?',
        (product_id,)
    ).fetchone()['avg']

    return render_template(
        'product.html',
        product=product,
        reviews=reviews,
        avg_rating=avg_rating
    )


@app.route('/admin')
def admin():
    db = get_db()
    feedback = db.execute('''
        SELECT
            f.id,
            p.name as product_name,
            f.reviewer_name,
            f.rating,
            f.comment,
            f.created_at
        FROM feedback f
        JOIN products p ON f.product_id = p.id
        ORDER BY f.created_at DESC
    ''').fetchall()
    return render_template('admin.html', feedback=feedback)


@app.route('/api/feedback', methods=['POST'])
def submit_feedback():
    data = request.get_json(silent=True)
    if not data:
        return jsonify({'error': 'JSON body required'}), 400

    product_id = data.get('product_id')
    rating = data.get('rating')
    comment = data.get('comment', '').strip()
    reviewer_name = data.get('reviewer_name', 'Anonymous').strip() or 'Anonymous'

    if product_id is None:
        return jsonify({'error': 'product_id is required'}), 400

    if rating is None:
        return jsonify({'error': 'rating is required'}), 400

    try:
        rating = int(rating)
    except (TypeError, ValueError):
        return jsonify({'error': 'rating must be an integer'}), 400

    if not (1 <= rating <= 5):
        return jsonify({'error': 'rating must be between 1 and 5'}), 400

    if not comment:
        return jsonify({'error': 'comment is required'}), 400

    db = get_db()
    product = db.execute(
        'SELECT id FROM products WHERE id = ?', (product_id,)
    ).fetchone()

    if product is None:
        return jsonify({'error': 'product not found'}), 404

    cursor = db.execute(
        'INSERT INTO feedback (product_id, rating, comment, reviewer_name) VALUES (?, ?, ?, ?)',
        (product_id, rating, comment, reviewer_name)
    )
    db.commit()

    return jsonify({'success': True, 'id': cursor.lastrowid}), 200


if __name__ == '__main__':
    init_db()
    app.run(debug=True)
