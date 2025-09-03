from flask import Blueprint, render_template_string, request, redirect, url_for, flash
from flask_login import login_user, login_required, logout_user, current_user
from controller import db, User, Workout
import html

api_v1 = Blueprint('api_v1', __name__)


@api_v1.route('/')
def home():
    return render_template_string(html.home_html)


@api_v1.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if User.query.filter_by(username=username).first():
            flash('Username already exists.')
            return redirect(url_for('api_v1.register'))
        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()
        flash('Registration successful. Please log in.')
        return redirect(url_for('api_v1.login'))
    return render_template_string(html.register_html)


@api_v1.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username, password=password).first()
        if user:
            login_user(user)
            return redirect(url_for('api_v1.dashboard'))
        else:
            flash('Invalid credentials.')
    return render_template_string(html.login_html)


@api_v1.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out successfully.')
    return redirect(url_for('api_v1.home'))


@api_v1.route('/dashboard')
@login_required
def dashboard():
    workouts = Workout.query.filter_by(user_id=current_user.id).all()
    return render_template_string(html.dashboard_html, workouts=workouts)


@api_v1.route('/add', methods=['GET', 'POST'])
@login_required
def add_workout():
    if request.method == 'POST':
        workout = request.form['workout']
        duration = request.form['duration']
        category = request.form['category']
        try:
            duration_int = int(duration)
            new_workout = Workout(
                user_id=current_user.id,
                workout=workout,
                duration=duration_int,
                category=category
            )
            db.session.add(new_workout)
            db.session.commit()
            flash('Workout added!')
            return redirect(url_for('api_v1.dashboard'))
        except ValueError:
            flash('Duration must be a number.')
    return render_template_string(html.add_html)
