from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_required, current_user
from models.quiz import Topic, TopicProgress
from models.score import Score

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    all_topics = Topic.query.order_by(Topic.order).all()
    basic_topics = [t for t in all_topics if (t.level or 'Basic') == 'Basic']
    intermediate_topics = [t for t in all_topics if t.level == 'Intermediate']
    advanced_topics = [t for t in all_topics if t.level == 'Advanced']
    return render_template('index.html',
                           topics=all_topics,
                           basic_topics=basic_topics,
                           intermediate_topics=intermediate_topics,
                           advanced_topics=advanced_topics)

@main_bp.route('/topics')
def topics():
    level_filter = request.args.get('level', '').strip().capitalize()
    all_topics = Topic.query.order_by(Topic.order).all()
    basic_topics = [t for t in all_topics if (t.level or 'Basic') == 'Basic']
    intermediate_topics = [t for t in all_topics if t.level == 'Intermediate']
    advanced_topics = [t for t in all_topics if t.level == 'Advanced']
    
    return render_template('topics.html', 
                           topics=all_topics,
                           basic_topics=basic_topics,
                           intermediate_topics=intermediate_topics,
                           advanced_topics=advanced_topics,
                           active_level=level_filter)

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
    all_topics = Topic.query.order_by(Topic.order).all()
    total_topics = len(all_topics)
    
    # Progress records
    completed_records = TopicProgress.query.filter_by(
        user_id=current_user.id, completed=True).all()
    completed_topic_ids = {p.topic_id for p in completed_records}
    completed_topics = len(completed_topic_ids)
    
    # Per-tier progress calculations
    basic_topics = [t for t in all_topics if (t.level or 'Basic') == 'Basic']
    intermediate_topics = [t for t in all_topics if t.level == 'Intermediate']
    advanced_topics = [t for t in all_topics if t.level == 'Advanced']
    
    basic_completed = sum(1 for t in basic_topics if t.id in completed_topic_ids)
    intermediate_completed = sum(1 for t in intermediate_topics if t.id in completed_topic_ids)
    advanced_completed = sum(1 for t in advanced_topics if t.id in completed_topic_ids)
    
    basic_pct = int((basic_completed / len(basic_topics) * 100)) if basic_topics else 0
    intermediate_pct = int((intermediate_completed / len(intermediate_topics) * 100)) if intermediate_topics else 0
    advanced_pct = int((advanced_completed / len(advanced_topics) * 100)) if advanced_topics else 0
    
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
        progress_pct=progress_pct,
        basic_topics=basic_topics,
        intermediate_topics=intermediate_topics,
        advanced_topics=advanced_topics,
        basic_completed=basic_completed,
        intermediate_completed=intermediate_completed,
        advanced_completed=advanced_completed,
        basic_pct=basic_pct,
        intermediate_pct=intermediate_pct,
        advanced_pct=advanced_pct
    )
