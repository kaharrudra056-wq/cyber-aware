from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from models import db
from models.quiz import Topic, Question
from models.score import Score

quiz_bp = Blueprint('quiz', __name__)

@quiz_bp.route('/quiz/<int:topic_id>')
@login_required
def start_quiz(topic_id):
    topic = Topic.query.get_or_404(topic_id)
    questions = Question.query.filter_by(topic_id=topic_id).all()
    if not questions:
        flash('No questions available for this topic yet.', 'warning')
        return redirect(url_for('main.topics'))
    return render_template('quiz.html', topic=topic, questions=questions)

@quiz_bp.route('/quiz/<int:topic_id>/submit', methods=['POST'])
@login_required
def submit_quiz(topic_id):
    topic = Topic.query.get_or_404(topic_id)
    questions = Question.query.filter_by(topic_id=topic_id).all()
    score = 0
    results = []
    for q in questions:
        user_answer = request.form.get(f'q{q.id}', '').upper()
        is_correct = user_answer == q.correct_answer.upper()
        if is_correct:
            score += 1
        results.append({
            'question': q.question_text,
            'user_answer': user_answer,
            'correct_answer': q.correct_answer,
            'is_correct': is_correct,
            'explanation': q.explanation,
            'options': {
                'A': q.option_a, 'B': q.option_b,
                'C': q.option_c, 'D': q.option_d
            }
        })
    total = len(questions)
    percentage = round((score / total * 100), 1) if total else 0
    # Save score
    new_score = Score(
        user_id=current_user.id,
        topic_id=topic_id,
        score=score,
        total=total,
        percentage=percentage
    )
    db.session.add(new_score)
    db.session.commit()
    return render_template('result.html',
        topic=topic, score=score, total=total,
        percentage=percentage, results=results
    )
