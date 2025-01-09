from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/love',methods=['GET'])
def affinity():
    # get lovers
    lover1 = request.args.get('lover1').lower()
    lover2 = request.args.get('lover2').lower()
    # compute affinity
    affinity = (hash(lover1) + hash(lover2))%101
    # prepare & send reply
    reply = {}
    reply['lover1'] = lover1
    reply['lover2'] = lover2
    reply['affinity'] = affinity
    return jsonify(reply)

if __name__ == '__main__':
    app.run(port=50000)


    