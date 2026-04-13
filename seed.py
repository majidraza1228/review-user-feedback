#!/usr/bin/env python3
"""
Seed FeedbackLoop with 6 products and 20 feedback entries.
Run after starting the app: python seed.py
"""

import sqlite3
import sys

DATABASE = 'database.db'

PRODUCTS = [
    (1, 'Notion AI', 'Productivity', 'All-in-one workspace with AI writing assistant, databases, and docs. Used by 30M+ teams worldwide.'),
    (2, 'Linear', 'Project Management', 'Modern issue tracker built for high-performance software teams. Fast, opinionated, and keyboard-first.'),
    (3, 'Raycast', 'Developer Tools', 'Blazingly fast macOS launcher. Replace Spotlight with a scriptable command palette for developers.'),
    (4, 'Superhuman', 'Email', 'The fastest email experience ever made. AI triage, keyboard shortcuts, and split-second send.'),
    (5, 'Cron', 'Calendar', 'Next-generation calendar for professionals and teams. Unified view across all your Google calendars.'),
    (6, 'Loom', 'Communication', 'Record your screen and camera to share quick video messages instead of long meetings or long emails.'),
]

FEEDBACK = [
    # Notion AI (product_id=1)
    (1, 5, 'The AI writing assistant saves me 2 hours a week on docs. The database views are unmatched.', 'Jordan K.'),
    (1, 4, 'Incredibly powerful but there is a learning curve. Took me 2 weeks to set up my system properly.', 'Sam R.'),
    (1, 5, 'Replaced Confluence, Trello, and Google Docs for our team. The AI summarization is surprisingly good.', 'Alex M.'),
    (1, 4, 'Solid product. Wish the mobile app was faster. Desktop experience is a 10/10 though.', 'Taylor B.'),
    # Linear (product_id=2)
    (2, 5, 'The keyboard shortcuts alone justify switching from Jira. Cycles and roadmaps are excellent.', 'Morgan L.'),
    (2, 4, 'Fast and opinionated in a good way. Integrations with GitHub are seamless.', 'Casey W.'),
    (2, 4, 'Our team of 8 shipped 40% more in Q1 after switching. Hard to attribute entirely to Linear but it helped.', 'Riley H.'),
    (2, 3, 'Great for engineering teams. Less useful if your team is cross-functional with non-technical members.', 'Drew P.'),
    # Raycast (product_id=3)
    (3, 5, 'Replaced Alfred and Spotlight. The extensions ecosystem is incredible. Clipboard history alone is worth it.', 'Jordan K.'),
    (3, 5, 'Every developer on our team uses it within a week of joining. That says everything.', 'Sam R.'),
    (3, 4, 'The AI feature is surprisingly useful for quick lookups. Extension development is easy if you know React.', 'Alex M.'),
    # Superhuman (product_id=4)
    (4, 4, 'The speed is real. I get through email 3x faster than Gmail. Expensive but worth it for the time savings.', 'Casey W.'),
    (4, 3, 'Great UX but the price ($30/mo) is hard to justify for most users. Wish there was a cheaper tier.', 'Morgan L.'),
    (4, 5, 'The AI triage is the best email feature I have used. Automatically surfaces what needs a reply.', 'Riley H.'),
    (4, 2, 'Too opinionated. Forces you into their workflow. If you are not a keyboard power user, skip it.', 'Drew P.'),
    # Cron (product_id=5)
    (5, 4, 'The unified calendar view across all my Google accounts changed how I plan my week.', 'Taylor B.'),
    (5, 3, 'Good concept but still feels like a beta product. Missing some features I expected.', 'Jordan K.'),
    (5, 4, 'Keyboard shortcuts make scheduling so much faster than Google Calendar.', 'Sam R.'),
    # Loom (product_id=6)
    (6, 5, 'Cut our meeting count by 30%. Async video updates work better than I expected for our remote team.', 'Alex M.'),
    (6, 4, 'The transcription and search features are underrated. I can find any video by searching the transcript.', 'Casey W.'),
]


def seed():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    # Check if already seeded
    count = cursor.execute('SELECT COUNT(*) FROM products').fetchone()[0]
    if count > 0:
        print(f'Database already has {count} products. Skipping seed.')
        print('To re-seed: delete database.db and run python app.py first, then python seed.py')
        conn.close()
        return

    # Insert products
    cursor.executemany(
        'INSERT INTO products (id, name, category, description) VALUES (?, ?, ?, ?)',
        PRODUCTS
    )

    # Insert feedback
    cursor.executemany(
        'INSERT INTO feedback (product_id, rating, comment, reviewer_name) VALUES (?, ?, ?, ?)',
        FEEDBACK
    )

    conn.commit()
    conn.close()

    print(f'Seeded {len(PRODUCTS)} products and {len(FEEDBACK)} feedback entries.')
    print('Visit http://localhost:5000 to see the app.')


if __name__ == '__main__':
    seed()
