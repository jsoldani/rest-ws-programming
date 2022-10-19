from flask import Flask, request, jsonify

app = Flask(__name__)

scores = {} # indexed by players, storing associated scores

@app.route('/scores',methods=['POST'])
def add_score() :
    # get request's JSON body
    body = request.json 
    # return error if player already exists
    player = body['player']
    if player in scores: 
        return jsonify({ "error": True }) 
    # add new player (with given score, or 0 by default)
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

@app.route('/scores/<player>',methods=['GET'])
def get_score(player):
    # return error if player doesn't exist
    if player not in scores: 
        return jsonify({ "error": True }) 
    # prepare & send reply
    reply = {}
    reply['player'] = player
    reply['score'] = scores[player]
    return jsonify(reply)

@app.route('/scores/<player>',methods=['PUT'])
def update_score(player):
    # return error if player doesn't exist
    if player not in scores: 
        return jsonify({ "error": True }) 
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
        return jsonify({ "error": True }) 
    # remove player
    scores.pop(player)
    # send reply
    return jsonify({})

if __name__ == '__main__':
    app.run(port=50000)