from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/calc/<operator>',methods=['GET'])
def execute(operator):
    # parse input parameters n,m
    n = int(request.args.get('n'))
    m = int(request.args.get('m'))
    # build reply depending on operator
    reply = {}
    reply['n'] = n
    reply['m'] = m
    if operator == 'sum':
        reply['result'] = n+m
        reply['op'] = '+'
    elif operator == 'difference':
        reply['result'] = n-m
        reply['op'] = '-'
    elif operator == 'product':
        reply['result'] = n*m
        reply['op'] = '*'
    elif operator == 'division':
        reply['result'] = n/m
        reply['remainder'] = n%m
        reply['op'] = '/'
    else:
        return jsonify({'error':True}) # if unknown operator, return error
    # send reply
    return jsonify(reply)

if __name__ == '__main__':
    app.run(port=50000)


