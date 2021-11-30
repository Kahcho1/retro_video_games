from application import app
from application.forms import GamesForm, ConsoleForm
from flask import render_template, request, redirect, url_for, jsonify
import requests

backend_host = "retro_video_games_backend:5000"

@app.route('/')
@app.route('/home')
def home():
    all_games = requests.get(f"http://{backend_host}/read/vgdb").json()
    app.logger.info(f"Games: {all_games}")
    return render_template('index.html', title="Home Page", all_games=all_games["games"])

@app.route('/add/game', methods=['GET', 'POST'])
def add_game():
    form = GamesForm()

    if request.method == "POST":
        response = requests.post(
            f"http://{backend_host}/add/game",
            json={"name": form.name.data}
            )
        app.logger.info(f"Response: {response.text}")
        return redirect(url_for('home'))

    return render_template("create_game_form.html", title="Adding new game entry", form=form)

@app.route('/add/platform', methods=['GET', 'POST'])
def add_platform():
    form = ConsoleForm()

    if request.method == "POST":
        response = requests.post(
            f"http://{backend_host}/add/platform",
            json={"name": form.name.data}
            )
        app.logger.info(f"Response: {response.text}")
        return redirect(url_for('home'))

    return render_template("create_console_form.html", title="Adding a platform", form=form)

# @app.route('/update/task/<int:id>', methods=['GET', 'POST'])
# def update_task(id):
#     form = TaskForm()
#     task = requests.get(
#         f"http://{backend_host}/read/tasks/{id}").json()
#     app.logger.info(f"Tasks: {task}")

#     if request.method == "POST":
#         response = requests.put(
#             f"http://{backend_host}/update/task/{id}",
#             json={"description": form.desc.data}
#             )
#         return redirect(url_for('home'))

#     return render_template('update_task_form.html', task=task, form=form)

# @app.route('/delete/task/<int:id>')
# def delete(id):
#     response = requests.delete(f"http://{backend_host}/delete/task/{id}")
#     app.logger.info(f"Response: {response.text}")
#     return redirect(url_for('home'))
