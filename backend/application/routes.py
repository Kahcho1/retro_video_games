from application import app, db
from application.models import Games, Console
from flask import request, redirect, url_for, Response, jsonify

@app.route('/add/game', methods=['POST'])
def add_game():
    package = request.json

    new_game = Games(
        game_name=package["name"], 
        description=package["description"], 
        date=package["release_date"],
        consoles_id=package["console"]
    )
    db.session.add(new_game)
    db.session.commit()
    return Response(f"{new_game.game_name} has been added to Games!", mimetype='text/plain')

@app.route('/add/platform', methods=['POST'])
def add_platform():
    package = request.json

    new_console = Console(
        console_name=package["name"], 
        date=package["release_date"]
    )
    db.session.add(new_console)
    db.session.commit()
    return Response(f"{new_console.console_name} has been added to Consoles!", mimetype='text/plain')

@app.route('/read/vgdb', methods=['GET'])
def read_game():
    list_game = Games.query.all()
    game_dict = {"games": []}

    for game in list_game:
        game_dict["games"].append(
            {
                "id": game.id,
                "name": game.game_name,
                "release_date": game.date,
                "description": game.description,
                "console": game.console.console_name
            }
        )
    return jsonify(game_dict)

@app.route('/read/cdb', methods=['GET'])
def read_console():
    list_console = Console.query.all()
    console_dict = {"console": []}

    for console in list_console:
        games = []
        for game in console.games:
            games.append(
            {
                "id": game.id,
                "name": game.game_name,
                "release_date": game.date,
                "description": game.description
            }
        )
        console_dict["console"].append(
            {
                "id": console.id,
                "name": console.console_name,
                "release_date": console.date,
                "games": games
            }
        )
    return jsonify(console_dict)

@app.route('/read/vgdb/<int:id>', methods=['GET'])
def read_game_one(id):
    game = Games.query.get(id)
    game_dict ={
                "id": game.id,
                "name": game.game_name,
                "release_date": game.date,
                "description": game.description,
                "console": game.console.console_name
            }
    return jsonify(game_dict)

@app.route('/read/cdb/<int:id>', methods=['GET'])
def read_console_one(id):
    console = Console.query.get(id)
    console_dict ={
                    "id": console.id,
                    "name": console.console_name,
                    "release_date": console.date
                }
    return jsonify(console_dict)

@app.route('/update/game/<int:id>', methods=['PUT'])
def update_game(id):
    package = request.json
    game = Games.query.get(id)
    game.game_name = package["name"]
    game.date = package["release_date"]
    game.description = package["description"]
    game.console.console_name = package["console"]
    db.session.commit()
    return Response(f"{game.game_name} information has been updated!.", mimetype='text/plain')

@app.route('/update/platform/<int:id>', methods=['PUT'])
def update_platform(id):
    package = request.json
    console = Console.query.get(id)
    console.console_name = package["name"]
    console.date = package["release_date"]
    db.session.commit()
    return Response(f"{console.console_name} information has been updated under Platforms", mimetype='text/plain')


@app.route('/delete/game/<int:id>', methods=['DELETE'])
def delete(id):
    game = Games.query.get(id)
    db.session.delete(game)
    db.session.commit()
    return Response(f"{game.game_name} has been deleted!", mimetype='text/plain')

@app.route('/delete/platform/<int:id>', methods=['DELETE'])
def delete_platform(id):
    console = Console.query.get(id)
    db.session.delete(console)
    db.session.commit()
    return Response(f"{console.console_name} has been deleted!", mimetype='text/plain')