from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # Povolit CORS, aby frontend mohl volat API

# Konfigurace připojení k MySQL
# Upravte 'username', 'password' a případně 'localhost' dle potřeby.
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://username:password@localhost/books_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Model pro knihy
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(100), nullable=False)
    title = db.Column(db.String(200), nullable=False)

# Endpoint pro uložení knihy
@app.route('/api/book', methods=['POST'])
def add_book():
    data = request.get_json()
    author = data.get('author')
    title = data.get('title')
    if not author or not title:
        return jsonify({'message': 'Missing author or title'}), 400
    new_book = Book(author=author, title=title)
    db.session.add(new_book)
    db.session.commit()
    return jsonify({'message': 'Book added successfully'}), 201

# Endpoint pro vyhledání knih podle klíčového slova
@app.route('/api/search', methods=['GET'])
def search_books():
    keyword = request.args.get('keyword', '')
    books = Book.query.filter(
        (Book.author.ilike(f"%{keyword}%")) | (Book.title.ilike(f"%{keyword}%"))
    ).all()
    results = []
    for book in books:
        results.append({
            'id': book.id,
            'author': book.author,
            'title': book.title
        })
    return jsonify(results)

if __name__ == '__main__':
    # Pokud databáze ještě nebyla inicializována, odkomentujte následující řádek a spusťte jednou:
    # db.create_all()
    app.run(host='0.0.0.0', port=5000)
