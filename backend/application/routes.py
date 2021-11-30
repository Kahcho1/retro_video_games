from application import app, db
from application.models import Games, Console
from flask import request, redirect, url_for, Response, jsonify

@app.route('/create/game', methods=['POST'])
def create_game():
    package = request.json
    game_new = Games(desc=package["description"])
    db.session.add(game_new)
    db.session.commit()
    return Response(f"Game with description has been added: {game_new.description}", mimetype='text/plain')

@app.route('/read/allGames', methods=['GET'])
def read_games():
    all_games = Games.query.all()
    g_dict = {"games": []}

    for games in all_games:
        g_dict["games"].append(
            {
                "id": games.id,
                "Name": games.gname,
                "description": games.description,
                "Release Date": games.gdate
            }
        )
    return jsonify(g_dict)

@app.route('/read/games/<int:id>', methods=['GET'])
def read_game(id):
    game = Tasks.query.get(id)
    g_dict = {
                "id": games.id,
                "Name": games.gname,
                "description": games.description,
                "Release Date": games.gdate
            }
    return jsonify(g_dict)

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