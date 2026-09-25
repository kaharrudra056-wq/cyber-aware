from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user
from models.quiz import Topic, TopicProgress
from models.score import Score

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    topics = Topic.query.order_by(Topic.order).all()
    return render_template('index.html', topics=topics)

@main_bp.route('/topics')
def topics():
    all_topics = Topic.query.order_by(Topic.order).all()
    return render_template('topics.html', topics=all_topics)

@main_bp.route('/topics/<slug>')
@login_required
def topic_detail(slug):
    topic = Topic.query.filter_by(slug=slug).first_or_404()
    # Mark topic as completed when user reads it
    progress = TopicProgress.query.filter_by(
        user_id=current_user.id, topic_id=topic.id).first()
    if not progress:
        from models import db
        from datetime import datetime
        progress = TopicProgress(
            user_id=current_user.id,
            topic_id=topic.id,
            completed=True,
            completed_at=datetime.utcnow()
        )
        db.session.add(progress)
        db.session.commit()
    return render_template('topic_detail.html', topic=topic)

@main_bp.route('/phishing')
def phishing():
    return render_template('phishing.html')

@main_bp.route('/dashboard')
@login_required
def dashboard():
    total_topics = Topic.query.count()
    completed_topics = TopicProgress.query.filter_by(
        user_id=current_user.id, completed=True).count()
    scores = Score.query.filter_by(user_id=current_user.id).order_by(
        Score.taken_at.desc()).all()
    latest_score = scores[0] if scores else None
    avg_score = 0
    if scores:
        avg_score = sum(s.percentage for s in scores) / len(scores)
    progress_pct = int((completed_topics / total_topics * 100)) if total_topics else 0
    return render_template('dashboard.html',
        total_topics=total_topics,
        completed_topics=completed_topics,
        scores=scores,
        latest_score=latest_score,
        avg_score=round(avg_score, 1),
        progress_pct=progress_pct
    )
