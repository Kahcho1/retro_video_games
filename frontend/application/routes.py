from application import app
from application.forms import GamesForm, ConsoleForm
from flask import render_template, request, redirect, url_for, jsonify
import requests

backend_host = "retro_video_games_backend:5000"

@app.route('/')
@app.route('/home')
def home():
    all_game = requests.get(f"http://{backend_host}/read/vgdb").json()
    app.logger.info(f"Game: {all_game}")
    return render_template('index.html', title="Home", all_game=all_game["games"])

@app.route('/home/console')
def home_console():
    all_console = requests.get(f"http://{backend_host}/read/cdb").json()
    return render_template('index_console.html', title="Consoles", all_console=all_console["console"])

@app.route('/add/game', methods=['GET', 'POST'])
def add_game():
    form = GamesForm()
    
    console = requests.get(f"http://{backend_host}/read/cdb").json()
    for console in console["console"]:
        form.console.choices.append((console["id"], console["name"])) 

    if request.method == "POST":
        response = requests.post(
            f"http://{backend_host}/add/game",
            json={
                "name": form.name.data,
                "release_date": str(form.date.data),
                "console": form.console.data,
                "description": form.description.data
                }
            )
        app.logger.info(f"Response: {response.text}")
        return redirect(url_for('home'))

    return render_template("create_game_form.html", title="New Game Entry", form=form)

@app.route('/add/platform', methods=['GET', 'POST'])
def add_platform():
    form = ConsoleForm()

    if request.method == "POST":
        response = requests.post(
            f"http://{backend_host}/add/platform",
            json={
                "name": form.name.data,
                "release_date": str(form.date.data)
                }
            )
        app.logger.info(f"Response: {response.text}")
        return redirect(url_for('home_console'))

    return render_template("create_console_form.html", title="New Console Entry", form=form)

@app.route('/update/game/<int:id>', methods=['GET', 'POST'])
def update_game(id):
    form = GamesForm()
    game = requests.get(
        f"http://{backend_host}/read/vgdb/{id}").json()
    app.logger.info(f"Games: {game}")

    if request.method == "POST":
        response = requests.put(
            f"http://{backend_host}/update/game/{id}",
            json={
                "name": form.name.data,
                "release_date": str(form.date.data),
                "console": form.console.data,
                "description": form.console.data
                }
            )
        return redirect(url_for('home'))

    return render_template('update_game_form.html', game=game, form=form)

@app.route('/delete/game/<int:id>')
def delete(id):
    response = requests.delete(f"http://{backend_host}/delete/game/{id}")
    app.logger.info(f"Response: {response.text}")
    return redirect(url_for('home'))

@app.route('/delete/platform/<int:id>')
def delete_platform(id):
    response = requests.delete(f"http://{backend_host}/delete/platform/{id}")
    app.logger.info(f"Response: {response.text}")
    return redirect(url_for('home_console'))