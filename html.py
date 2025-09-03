home_html = """
<!doctype html>
<title>ACEestFitness and Gym Tracker</title>
<h1>ACEestFitness and Gym Tracker</h1>
<a href="{{ url_for('api_v1.register') }}">Register</a> |
<a href="{{ url_for('api_v1.login') }}">Login</a>
"""

register_html = """
<h2>Register</h2>
<form method="post">
    Username: <input name="username"><br>
    Password: <input name="password" type="password"><br>
    <input type="submit" value="Register">
</form>
<a href="{{ url_for('api_v1.home') }}">Home</a>
"""

login_html = """
<h2>Login</h2>
<form method="post">
    Username: <input name="username"><br>
    Password: <input name="password" type="password"><br>
    <input type="submit" value="Login">
</form>
<a href="{{ url_for('api_v1.home') }}">Home</a>
"""

dashboard_html = """
<h2>Your Workouts</h2>
<a href="{{ url_for('api_v1.add_workout') }}">Add Workout</a> |
<a href="{{ url_for('api_v1.logout') }}">Logout</a>
<ul>
{% for w in workouts %}
    <li>{{ w.workout }} - {{ w.duration }} min ({{ w.category }})</li>
{% endfor %}
</ul>
"""

add_html = """
<h2>Add Workout</h2>
<form method="post">
    Workout: <input name="workout"><br>
    Duration (minutes): <input name="duration" type="number"><br>
    Category:
    <select name="category">
        <option>Cardio</option>
        <option>Strength</option>
        <option>Flexibility</option>
    </select><br>
    <input type="submit" value="Add">
</form>
<a href="{{ url_for('api_v1.dashboard') }}">Dashboard</a>
"""
