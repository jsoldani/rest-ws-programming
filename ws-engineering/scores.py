from flask import Flask, request, jsonify, Response

app = Flask(__name__)

scores = {} # indexed by players, storing associated scores

@app.route('/scores',methods=['POST'])
def add_score() :
    # get request's JSON body
    body = request.json 
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
        scores[player] = body['score']
    else: 
        scores[player] = 0
    # prepare & send reply 
    reply = {}
    reply["player"] = player
    reply["score"] = scores[player]
    reply["path"] = "/punteggi/" + player
    return jsonify(reply)

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

if __name__ == '__main__':
    app.run(port=50000)