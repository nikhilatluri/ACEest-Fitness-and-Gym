from controller import db, User, Workout


def register(client, username, password):
    return client.post('/register', data={
        'username': username,
        'password': password
    }, follow_redirects=True)


def login(client, username, password):
    return client.post('/login', data={
        'username': username,
        'password': password
    }, follow_redirects=True)


def logout(client):
    return client.get('/logout', follow_redirects=True)


def add_workout(client, workout, duration, category):
    return client.post('/add', data={
        'workout': workout,
        'duration': duration,
        'category': category
    }, follow_redirects=True)


def test_home_page(client):
    rv = client.get('/')
    assert b'ACEestFitness and Gym Tracker' in rv.data


def test_user_registration(client):
    rv = register(client, 'testuser', 'testpass')
    assert b'Login' in rv.data


def test_duplicate_registration(client):
    register(client, 'testuser', 'testpass')
    rv = register(client, 'testuser', 'testpass')
    assert b'Login' in rv.data


def test_login_logout(client):
    register(client, 'testuser', 'testpass')
    rv = login(client, 'testuser', 'testpass')
    assert b'Your Workouts' in rv.data
    rv = logout(client)
    assert b'ACEestFitness and Gym Tracker' in rv.data


def test_invalid_login(client):
    rv = login(client, 'nouser', 'nopass')
    assert b'Login' in rv.data


def test_add_workout(client):
    register(client, 'testuser', 'testpass')
    login(client, 'testuser', 'testpass')
    rv = add_workout(client, 'Running', 30, 'Cardio')
    assert b'Your Workouts' in rv.data
    assert b'Running' in rv.data
    assert b'30 min' in rv.data
    assert b'Cardio' in rv.data


def test_dashboard_requires_login(client):
    rv = client.get('/dashboard', follow_redirects=True)
    assert b'Login' in rv.data


def test_add_requires_login(client):
    rv = client.get('/add', follow_redirects=True)
    assert b'Login' in rv.data


def test_add_workout_invalid_duration(client):
    register(client, 'testuser', 'testpass')
    login(client, 'testuser', 'testpass')
    rv = add_workout(client, 'Yoga', 'notanumber', 'Flexibility')
    assert b'Add Workout' in rv.data
