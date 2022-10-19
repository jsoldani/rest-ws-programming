from flask import Flask, request, jsonify

app = Flask(__name__)

items = {}

@app.route('/inventory',methods=['POST'])
def add_item():
    body = request.json
    code = body['code']
    # if code already used, reply error
    if code in items:
        return jsonify({'error':True})
    # add item to inventory
    description = 'nd'
    if 'description' in body: 
        description = body['description']
    quantity = 0
    if 'quantity' in body: 
        quantity = body['quantity']
    items[code] = {
        'description': description,
        'quantity': quantity
    }
    # build & send reply
    path = '/inventory/'+code
    return jsonify({
        'path': path,
        'code': code,
        'description': description,
        'quantity': quantity
    })

@app.route('/inventory/<code>',methods=['GET'])
def get_item(code):
    # if code unknown, return error
    if code not in items:
        return jsonify({'error':True})
    # build & send reply
    return jsonify({
        'code': code,
        'description': items[code]['description'],
        'quantity': items[code]['quantity']
    })

@app.route('/inventory/<code>',methods=['PUT'])
def update_item(code):
    body = request.json
    code = body['code']
    # if code unknown, return error
    if code not in items:
        return jsonify({'error':True})
    # update item in inventory
    description = 'nd'
    if 'description' in body: 
        description = body['description']
    quantity = body['quantity']
    items[code] = {
        'description': description,
        'quantity': quantity
    }
    # build & send reply
    path = '/inventory/'+code
    return jsonify({
        'code': code,
        'description': description,
        'quantity': quantity
    })

@app.route('/inventory/<code>',methods=['DELETE'])
def delete_item(code):
    # if code unknown, return error
    if code not in items:
        return jsonify({'error':True})
    # delete item
    items.pop(code)
    # build & send reply
    return jsonify({})

if __name__ == '__main__':
    app.run(port=50000)


