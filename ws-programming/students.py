from flask import Flask, request, jsonify

app = Flask(__name__)

students = {} 

@app.route('/students',methods=['POST'])
def add_student():
    body = request.json
    id = body['id']
    # if id already in use, return error
    if id in students:
        return jsonify({'error':True})
    # add student
    surname = body['surname']
    name = body['name']
    students[id] = {
        'surname': surname,
        'name': name,
        'courses': {}
    }
    # build & send reply
    path = '/students/'+id
    return jsonify({
        'path': path,
        'id': id,
        'surname': students[id]['surname'],
        'name': students[id]['name'],
        'courses': students[id]['courses'],
    })

@app.route('/students/<id>',methods=['GET'])
def get_student(id):
    # if id not used, return error
    if id not in students:
        return jsonify({'error':True})
    # build & send reply
    return jsonify({
        'id': id,
        'surname': students[id]['surname'],
        'name': students[id]['name'],
        'courses': students[id]['courses'],
    })

@app.route('/students/<id>',methods=['PUT'])
def update_student(id):
    # if id not used, return error
    if id not in students:
        return jsonify({'error':True})
    # get course+grade
    course = request.args.get('course')
    grade = request.args.get('grade')
    # add new student's grade
    if course not in students[id]['courses']:
        students[id]['courses'][course] = []
    students[id]['courses'][course].append(grade)
    # build & send reply
    return jsonify({
        'id': id,
        'surname': students[id]['surname'],
        'name': students[id]['name'],
        'courses': students[id]['courses'],
    })

@app.route('/students/<id>',methods=['DELETE'])
def delete_student(id):
    # if id not used, return error
    if id not in students:
        return jsonify({'error':True})
    # delete student
    students.pop(id)
    return jsonify({})

if __name__ == '__main__':
    app.run(port=50000)
