from flask import Blueprint, request, jsonify, render_template
from helpers import token_required
from models import db, User, Book, book_schema, books_schema

api = Blueprint('api', '__name__', url_prefix='/api')

@api.route('/books', methods = ['POST'])
@token_required
def create_book(current_user_token):
    print(current_user_token)
    title = request.json['title']
    author = request.json['author']
    num_pages = request.json['num_pages']
    format = request.json['format']
    year_of_release = request.json['year_of_release']
    isbn = request.json['isbn']

    user_token = current_user_token.token


    book = Book(title, author, num_pages, format, year_of_release, isbn, user_token=user_token)
    print(book)

    db.session.add(book)
    db.session.commit()

    response = book_schema.dump(book)
    return jsonify(response)


@api.route('/books', methods = ['GET'])
@token_required
def get_book(current_user_token):
    a_user = current_user_token.token
    books = Book.query.filter_by(user_token = a_user).all()
    response = books_schema.dump(books)
    return jsonify(response)

@api.route('/books/<id>', methods = ['GET'])
@token_required
def get_single_book(current_user_token, id):
    book = Book.query.get(id)
    response = book_schema.dump(book)
    return jsonify(response)

@api.route('/books/<id>', methods = ['POST', 'PUT'])
@token_required
def update_book(current_user_token, id):
    book = Book.query.get(id)
    book.title = request.json['title']
    book.author = request.json['author']
    book.num_pages = request.json['num_pages']
    book.format = request.json['format']
    book.year_of_release = request.json['year_of_release']
    book.isbn = request.json['isbn']
    book.user_token = current_user_token.token

    db.session.commit()
    response = book_schema.dump(book)
    return jsonify(response)

@api.route('/books/<id>', methods = ['DELETE'])
@token_required
def delete_book(current_user_token, id):
    book = Book.query.get(id)
    db.session.delete(book)
    db.session.commit()
    response = book_schema.dump(book)
    return jsonify(response)
