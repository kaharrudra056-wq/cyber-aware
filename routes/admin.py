from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from models import db
from models.quiz import Topic, Question
from models.score import Score
from models.user import User
from functools import wraps

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

def admin_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not current_user.is_authenticated or not current_user.is_admin:
            flash('Admin access required.', 'danger')
            return redirect(url_for('main.index'))
        return f(*args, **kwargs)
    return decorated

@admin_bp.route('/')
@login_required
@admin_required
def dashboard():
    users = User.query.all()
    topics = Topic.query.all()
    questions = Question.query.all()
    scores = Score.query.order_by(Score.taken_at.desc()).limit(20).all()
    return render_template('admin/dashboard.html',
        users=users, topics=topics,
        questions=questions, scores=scores
    )

@admin_bp.route('/questions')
@login_required
@admin_required
def questions():
    all_questions = Question.query.join(Topic).order_by(Topic.title).all()
    topics = Topic.query.all()
    return render_template('admin/questions.html',
        questions=all_questions, topics=topics)

@admin_bp.route('/questions/add', methods=['GET', 'POST'])
@login_required
@admin_required
def add_question():
    topics = Topic.query.all()
    if request.method == 'POST':
        topic_id = request.form.get('topic_id')
        question_text = request.form.get('question_text', '').strip()
        option_a = request.form.get('option_a', '').strip()
        option_b = request.form.get('option_b', '').strip()
        option_c = request.form.get('option_c', '').strip()
        option_d = request.form.get('option_d', '').strip()
        correct = request.form.get('correct_answer', '').upper()
        explanation = request.form.get('explanation', '').strip()
        if not all([topic_id, question_text, option_a, option_b, option_c, option_d, correct]):
            flash('All fields except explanation are required.', 'danger')
            return render_template('admin/add_question.html', topics=topics)
        q = Question(
            topic_id=topic_id,
            question_text=question_text,
            option_a=option_a, option_b=option_b,
            option_c=option_c, option_d=option_d,
            correct_answer=correct,
            explanation=explanation
        )
        db.session.add(q)
        db.session.commit()
        flash('Question added successfully!', 'success')
        return redirect(url_for('admin.questions'))
    return render_template('admin/add_question.html', topics=topics)

@admin_bp.route('/questions/delete/<int:qid>', methods=['POST'])
@login_required
@admin_required
def delete_question(qid):
    q = Question.query.get_or_404(qid)
    db.session.delete(q)
    db.session.commit()
    flash('Question deleted.', 'info')
    return redirect(url_for('admin.questions'))

@admin_bp.route('/topics/add', methods=['GET', 'POST'])
@login_required
@admin_required
def add_topic():
    if request.method == 'POST':
        title = request.form.get('title', '').strip()
        slug = title.lower().replace(' ', '-')
        icon = request.form.get('icon', '🔒')
        description = request.form.get('description', '').strip()
        content = request.form.get('content', '').strip()
        order = request.form.get('order', 0)
        topic = Topic(title=title, slug=slug, icon=icon,
                      description=description, content=content, order=order)
        db.session.add(topic)
        db.session.commit()
        flash('Topic added!', 'success')
        return redirect(url_for('admin.dashboard'))
    return redirect(url_for('admin.dashboard'))
