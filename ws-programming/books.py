from flask import Flask, request, jsonify

app = Flask(__name__)

books = {} 

@app.route('/books',methods=['POST'])
def add_book():
    body = request.json
    # getting book info
    isbn = body['isbn']
    title = body['title']
    authors = body['authors']
    publisher = body['publisher']
    description = 'n.d.'
    if 'description' in body:
        description = body['description']
    # if isbn already present, reply with error
    if isbn in books:
        return jsonify({'error':True})
    # add book to books
    books[isbn] = {
        'title': title,
        'authors': authors,
        'publisher': publisher,
        'description': description
    }
    # build & send reply
    path = '/books/'+isbn
    return jsonify({
        'path': path,
        'isbn': isbn,
        'title': title,
        'authors': authors,
        'publisher': publisher,
        'description': publisher
    })

@app.route('/books/<isbn>',methods=['GET'])
def get_book(isbn):
    # if isbn unknown, return error
    if isbn not in books:
        return jsonify({'error':True})
    # build & send reply
    return jsonify(books[isbn])

@app.route('/books/<isbn>',methods=['PUT'])
def update_book(isbn):
    # if isbn unknown, return error
    if isbn not in books:
        return jsonify({'error':True})
    # getting book info
    body = request.json
    if isbn != body['isbn']:
        books.pop(isbn)
        isbn = body['isbn']
        books[isbn] = {}
    title = body['title']
    authors = body['authors']
    publisher = body['publisher']
    description = 'n.d.'
    if 'description' in body:
        description = body['description']
    books[isbn] = {
        'title': title,
        'authors': authors,
        'publisher': publisher,
        'description': description
    }
    # build & send reply
    path = '/books/'+isbn
    return jsonify({
        'path': path,
        'isbn': isbn,
        'title': title,
        'authors': authors,
        'publisher': publisher,
        'description': publisher
    })

@app.route('/books/<isbn>',methods=['DELETE'])
def delete_item(isbn):
    # if number unknown, return error
    if isbn not in books:
        return jsonify({'error':True})
    # delete item
    books.pop(isbn)
    # build & send reply
    return jsonify({})

if __name__ == '__main__':
    app.run(port=50000)


