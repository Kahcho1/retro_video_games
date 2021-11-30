from application import app, db
from application.models import Games, Console
from flask import request, redirect, url_for, Response, jsonify

@app.route('/add/game', methods=['POST'])
def add_game():
    package = request.json
    game_new = Games(game_name=package["game_name"], description=package["description"], date=package["date"])
    db.session.add(new_game)
    db.session.commit()
    return Response(f"{new_game.game_name} has been added to Games!", mimetype='text/plain')

@app.route('/add/platform', methods=['POST'])
def add_platform():
    package = request.json
    console_new = Console(console_name=package["console_name"], date=package["date"])
    db.session.add(new_console)
    db.session.commit()
    return Response(f"{new_console.console_name} has been added to Consoles!", mimetype='text/plain')

@app.route('/read/vgdb', methods=['GET'])
def read_vgdb():
    list_game = Games.query.all()
    game_dict = {"vgdb": []}

    for game in list_game:
        game_dict["vgdb"].append(
            {
                "id": game.id,
                "name": game.game_name,
                "release_date": game.date,
                "description": game.description,
                "console": game.console_name
            }
        )
    return jsonify(game_dict)

@app.route('/read/cdb', methods=['GET'])
def read_cdb():
    list_console = Console.query.all()
    console_dict = {"cdb": []}

    for console in list_console:
        game_dict["cdb"].append(
            {
                "id": console.id,
                "name": console.console_name,
                "release_date": console.date
            }
        )
    return jsonify(console_dict)

# @app.route('/update/task/<int:id>', methods=['PUT'])
# def update_task(id):
#     package = request.json
#     task = Tasks.query.get(id)
#     task.desc = package["description"]
#     db.session.commit()
#     return Response(f"Task #{id} has been updated with description: {task.desc}", mimetype='text/plain')

# @app.route('/delete/task/<int:id>', methods=['DELETE'])
# def delete(id):
#     task = Tasks.query.get(id)
#     db.session.delete(task)
#     db.session.commit()
#     return Response(f"Task #{id} has been deleted!", mimetype='text/plain')