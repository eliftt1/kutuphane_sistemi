from flask import Flask, render_template, request, redirect, url_for
from services.library import Library

app = Flask(__name__, template_folder='web/templates')
library = Library()

# Test için örnek veriler
library.add_book("Sefiller", "Victor Hugo", 1862)

@app.route('/')
def index():
    query = request.args.get('query')
    author_query = request.args.get('author')
    
    books = library.books
    if query:
        books = [b for b in books if query.lower() in b.name.lower()]
    elif author_query:
        books = [b for b in books if author_query.lower() in b.author.lower()]
        
    return render_template('index.html', books=books)

@app.route('/add', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        name = request.form['name']
        author = request.form['author']
        year = request.form['year']
        library.add_book(name, author, int(year))
        return redirect(url_for('index'))
    return render_template('add_book.html')

@app.route('/delete/<name>')
def delete_book(name):
    library.remove_book(name)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)