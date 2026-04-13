// FeedbackLoop — Star Rating Widget + Feedback Form
document.addEventListener('DOMContentLoaded', function () {
    const starRating = document.getElementById('star-rating');
    if (!starRating) return;

    const stars = starRating.querySelectorAll('.star-input');
    const ratingInput = document.getElementById('rating-value');
    const form = document.getElementById('feedback-form');

    // Star hover and click
    stars.forEach(function (star) {
        star.addEventListener('mouseenter', function () {
            const val = parseInt(this.dataset.value);
            stars.forEach(function (s) {
                s.classList.toggle('active', parseInt(s.dataset.value) <= val);
            });
        });

        star.addEventListener('mouseleave', function () {
            const selected = parseInt(ratingInput.value) || 0;
            stars.forEach(function (s) {
                s.classList.toggle('active', parseInt(s.dataset.value) <= selected);
            });
        });

        star.addEventListener('click', function () {
            ratingInput.value = this.dataset.value;
            const val = parseInt(this.dataset.value);
            stars.forEach(function (s) {
                s.classList.toggle('active', parseInt(s.dataset.value) <= val);
            });
            document.getElementById('rating-error').textContent = '';
        });
    });

    // Form submission
    form.addEventListener('submit', function (e) {
        e.preventDefault();

        const productId = parseInt(document.getElementById('product-id').value);
        const rating = parseInt(ratingInput.value);
        const comment = document.getElementById('comment').value.trim();
        const reviewerName = document.getElementById('reviewer-name').value.trim() || 'Anonymous';

        // Client-side validation
        let valid = true;
        if (!rating) {
            document.getElementById('rating-error').textContent = 'Please select a rating.';
            valid = false;
        }
        if (!comment) {
            document.getElementById('comment-error').textContent = 'Comment is required.';
            valid = false;
        } else {
            document.getElementById('comment-error').textContent = '';
        }
        if (!valid) return;

        const submitBtn = form.querySelector('button[type="submit"]');
        submitBtn.disabled = true;
        submitBtn.textContent = 'Submitting…';

        fetch('/api/feedback', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                product_id: productId,
                rating: rating,
                comment: comment,
                reviewer_name: reviewerName
            })
        })
        .then(function (res) { return res.json().then(function (data) { return { status: res.status, data: data }; }); })
        .then(function (result) {
            if (result.status === 200 && result.data.success) {
                document.getElementById('form-success').textContent = 'Review submitted! Refresh to see it.';
                form.reset();
                ratingInput.value = '';
                stars.forEach(function (s) { s.classList.remove('active'); });
            } else {
                document.getElementById('form-error').textContent = result.data.error || 'Something went wrong.';
            }
        })
        .catch(function () {
            document.getElementById('form-error').textContent = 'Network error. Please try again.';
        })
        .finally(function () {
            submitBtn.disabled = false;
            submitBtn.textContent = 'Submit Review';
        });
    });
});
