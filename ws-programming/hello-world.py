from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/hello',methods=['GET'])
def hello_world():
    whom = request.args.get("whom")
    return jsonify({'Hello':whom})

if __name__ == '__main__':
    app.run(port=50000)


