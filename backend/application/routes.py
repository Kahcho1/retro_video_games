from application import app, db
from application.models import Games, Console
from flask import request, redirect, url_for, Response, jsonify

@app.route('/add/game', methods=['POST'])
def add_game():
    package = request.json
    game_new = Games(game_name=package["game_name"])
    db.session.add(new_game)
    db.session.commit()
    return Response(f"{new_game.game_name} has been added to Games!", mimetype='text/plain')

@app.route('/add/date', methods=['POST'])
def add_date():
    package = request.json
    game_new = Games(date=package["date"])
    db.session.add(new_date)
    db.session.commit()
    return Response(f"{new_date.date} date has been added to database", mimetype='text/plain')

@app.route('/add/console', methods=['POST'])
def add_console():
    package = request.json
    console_new = Console(console_name=package["cname"])
    db.session.add(new_console)
    db.session.commit()
    return Response(f"{new_console.console_name} has been added to Consoles!", mimetype='text/plain')

@app.route('/read/vgdb', methods=['GET'])
def read_vgdb():
    all_games = Games.query.all()
    game_dict = {"vgdb": []}

    for game in vgdb:
        game_dict["vgdb"].append(
            {
                "id": game.id,
                "name": game.game_name,
                "release_date": game.date,
                "console": game.console_name
            }
        )
    return jsonify(game_dict)

# @app.route('/read/tasks/<int:id>', methods=['GET'])
# def read_task(id):
#     task = Tasks.query.get(id)
#     t_dict = {
#                 "id": task.id,
#                 "description": task.desc,
#                 "completed": task.comp
#             }
#     return jsonify(t_dict)

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