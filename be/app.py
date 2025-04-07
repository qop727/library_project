# BE Python Flask for library project.

from flask import Flask, request, jsonify # type: ignore
from flask_sqlalchemy import SQLAlchemy # type: ignore
from flask_cors import CORS # type: ignore

app = Flask(__name__)
CORS(app)                                                       # Enable CORS so FE can call APIs.

# MySQL connection configuration.
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://qop:Pwd1234@localhost/books_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False            # Turning off log for modifications.

db = SQLAlchemy(app)

# Model for books.
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)                # Setting DB column for ID of book.
    author = db.Column(db.String(100), nullable=False)          # Setting DB column for author of book (max 100 characters).
    title = db.Column(db.String(200), nullable=False)           # Setting DB column for title of book (max 200 characters).

# Endpoint for book saving.
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

# Endpoint for book search using key word.
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
    #with app.app_context():
        # Use this only once the DB was not yet incialized (first start only):
        #db.create_all()                                        # Creates DB table.
    app.run(host='0.0.0.0', port=5000)