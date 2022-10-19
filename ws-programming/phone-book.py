from flask import Flask, request, jsonify

app = Flask(__name__)

phonebook = {} 

def get_phonebook_key(surname,name):
    return surname+name

@app.route('/phonebook',methods=['POST'])
def add_number():
    body = request.json
    # getting contact info
    surname = body['surname']
    name = 'famiglia'
    if 'name' in body:
        name = body['name']
    number = body['number']
    # if number already present, reply error
    key = get_phonebook_key(surname,name)
    if key in phonebook:
        return jsonify({'error':True})
    # add number to phonebook
    phonebook[key] = {
        'surname': surname,
        'name': name,
        'number': number
    }
    # build & send reply
    path = '/phonebook/'+surname+'/'+name
    return jsonify({
        'path': path,
        'surname': surname,
        'name': name,
        'number': number
    })

@app.route('/phonebook/<surname>/<name>',methods=['GET'])
def get_number(surname,name):
    key = get_phonebook_key(surname,name)
    # if number unknown, return error
    if key not in phonebook:
        return jsonify({'error':True})
    # build & send reply
    return jsonify(phonebook[key])

@app.route('/phonebook/<surname>/<name>',methods=['PUT'])
def update_item(surname,name):
    key = get_phonebook_key(surname,name)
    # if number unknown, return error
    if key not in phonebook:
        return jsonify({'error':True})
    # update number
    number = request.args.get('number')
    phonebook[key]['number'] = number
    # build & send reply
    return jsonify(phonebook[key])

@app.route('/phonebook/<surname>/<name>',methods=['DELETE'])
def delete_item(surname,name):
    key = get_phonebook_key(surname,name)
    # if number unknown, return error
    if key not in phonebook:
        return jsonify({'error':True})
    # delete item
    phonebook.pop(key)
    # build & send reply
    return jsonify({})

if __name__ == '__main__':
    app.run(port=50000)


