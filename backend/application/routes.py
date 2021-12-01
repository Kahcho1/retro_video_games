from application import app, db
from application.models import Games, Console
from flask import request, redirect, url_for, Response, jsonify

@app.route('/add/game', methods=['POST'])
def add_game():
    package = request.json

    new_game = Games(
        name=package["name"], 
        description=package["description"], 
        date=package["date"]
    )
    db.session.add(new_game)
    db.session.commit()
    return Response(f"{new_game.game_name} has been added to Games!", mimetype='text/plain')

@app.route('/add/platform', methods=['POST'])
def add_platform():
    package = request.json

    new_console = Console(
        id=package["id"],
        console_name=package["console_name"], 
        date=package["date"]
    )
    db.session.add(new_console)
    db.session.commit()
    return Response(f"{new_console.console_name} has been added to Consoles!", mimetype='text/plain')

@app.route('/read/vgdb', methods=['GET'])
def read_game():
    list_game = Games.query.all()
    game_dict = {"games": []}

    for game in list_game:
        console = []
        for console in game.console:
            console.append(
            {
                "id": console.id,
                "name": console.console_name,
                "release_date": console.date
            }
        )
        game_dict["games"].append(
            {
                "id": game.id,
                "name": game.game_name,
                "release_date": game.date,
                "description": game.description,
                "console": console
            }
        )
    return jsonify(game_dict)

@app.route('/read/cdb', methods=['GET'])
def read_console():
    list_console = Console.query.all()
    console_dict = {"console": []}

    for console in list_console:
        game_dict["console"].append(
            {
                "id": console.id,
                "name": console.console_name,
                "release_date": console.date
            }
        )
    return jsonify(console_dict)

@app.route('/update/game/<int:id>', methods=['PUT'])
def update_game(id):
    package = request.json
    game = Games.query.get(id)
    game.game_name = package["name"]
    game.date = package["release_date"]
    game.description = package["description"]
    game.console = package["console"]
    db.session.commit()
    return Response(f"{game.game_name} information has been updated!.", mimetype='text/plain')

# @app.route('/update/platform/<int:id>', methods=['PUT'])
# def update_platform(id):
#     package = request.json
#     console = Console.query.get(id)
#     console.console_name = package["name"]
#     db.session.commit()
#     return Response(f"{console.console_name} information has been updated under Platforms", mimetype='text/plain')


@app.route('/delete/game/<int:id>', methods=['DELETE'])
def delete(id):
    game = Games.query.get(id)
    db.session.delete(game)
    db.session.commit()
    return Response(f"{game.game_name} has been deleted!", mimetype='text/plain')

# @app.route('/delete/platform/<int:id>', methods=['DELETE'])
# def delete(id):
#     console = Console.query.get(id)
#     db.session.delete(console)
#     db.session.commit()
#     return Response(f"{console.console_name} has been deleted!", mimetype='text/plain')