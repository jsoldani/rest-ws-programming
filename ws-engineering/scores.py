from flask import Flask, request, jsonify, Response
import json

app = Flask(__name__)

scores = {} # indexed by players, storing associated scores
users = {} # indexed by nickname, storing associated user info

# Removed, since now posting/deleting only users
'''
@app.route('/scores',methods=['POST'])
def add_score() :
    # get request's JSON body
    body = request.json 
    # return error if player is not indicated
    if 'player' not in body:
        response = Response("{'error': 'missing player'}",status=400,mimetype='application/json')
        return response
    # return error if player already exists
    player = body['player']
    if player in scores: 
        response = Response("{'error': 'already existing player'}",status=409,mimetype='application/json')
        return response
    # add new player (with given score, or 0 by default)
    if 'score' in body:
        scores[player] = body['score']
    else: 
        scores[player] = 0
    # prepare & send reply 
    response = Response(status=201)
    response.headers['Location'] = '/scores/' + player
    return response
'''

@app.route('/scores/<player>',methods=['GET'])
def get_score(player):
    # return error if player doesn't exist
    if player not in scores: 
        response = Response("{'error': 'player not found'}",status=404,mimetype='application/json')
        return response 
    # prepare & send reply
    reply = {}
    reply['player'] = player
    reply['score'] = scores[player]
    return jsonify(reply)

@app.route('/scores/<player>',methods=['PUT'])
def update_score(player):
    # return error if player doesn't exist
    if player not in scores: 
        response = Response("{'error': 'player not found'}",status=404,mimetype='application/json')
        return response 
    # get request's JSON body
    body = request.json 
    # update score (with given score, or 0 by default)
    if 'score' in body:
        score = int(body['score'])
        # if negative score, return error
        if score < 0:
            response = Response("{'error': 'negative score'}",status=400,mimetype='application/json')
            return response
        scores[player] = score
    else: 
        scores[player] = 0
    # prepare & send reply 
    reply = {}
    reply["player"] = player
    reply["score"] = scores[player]
    return jsonify(reply)

# Removed, now posting/deleting only users
'''
@app.route('/scores/<player>',methods=['DELETE'])
def remove_score(player):
    # return error if player doesn't exist
    if player not in scores: 
        response = Response("{'error': 'player not found'}",status=404,mimetype='application/json')
        return response 
    # remove player
    scores.pop(player)
    # send reply
    return jsonify({})
'''

@app.route('/users',methods=['POST'])
def add_user():
    # get request's JSON body
    body = request.json 
    # get nickname from body
    nickname = body['nickname']
    if nickname in users:
        return Response("{'error': 'already existing user'}",status=409,mimetype='application/json')
    # store user
    user = {}
    user['nickname'] = nickname
    if 'name' in body:
        user['name'] = body['name'] 
    else: 
        return Response("{'error': 'missing name'}",status=400,mimetype='application/json')
    if 'surname' in body:
        user['surname'] = body['surname'] 
    else: 
        return Response("{'error': 'missing surname'}",status=400,mimetype='application/json')
    if 'email' in body:
        user['email'] = body['email'] 
    else: 
        return Response("{'error': 'missing email'}",status=400,mimetype='application/json')
    users[nickname] = user
    # creating associated score
    scores[nickname] = 0
    # return stored user info
    user_string = json.dumps(user)
    response = Response(user_string,status=201,mimetype="application/json")
    response.headers['Location'] = '/user/' + nickname
    return response

@app.route('/users/<nickname>',methods=['PUT'])
def update_user(nickname):
    # check if existing user
    if nickname not in users:
        return Response("{'error': 'user not found'}",status=404,mimetype='application/json')
    # update user info
    body = request.json 
    if 'name' not in body and 'surname' not in body and 'email' not in body:
        return Response("{'error': 'at least a name, surname, or email should be specified'}",status=400,mimetype='application/json')
    if 'name' in body:
        users[nickname]['name'] = body['name']
    if 'surname' in body:
        users[nickname]['surname'] = body['surname']
    if 'email' in body:
        users[nickname]['email'] = body['email']
    # return response
    return jsonify(users[nickname])

@app.route('/users/<nickname>',methods=['GET'])
def get_user(nickname):
    # check if existing user
    if nickname not in users:
        return Response("{'error': 'user not found'}",status=404,mimetype='application/json')
    # return response
    return jsonify(users[nickname])

@app.route('/users/<nickname>',methods=['DELETE'])
def delete_user(nickname):
    # check if existing user
    if nickname not in users:
        return Response("{'error': 'user not found'}",status=404,mimetype='application/json')
    # remove player
    users.pop(nickname)
    scores.pop(nickname)
    # send reply
    return jsonify({})

if __name__ == '__main__':
    app.run(port=50000)