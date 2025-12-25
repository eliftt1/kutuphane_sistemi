from flask import Flask, render_template, request, redirect, url_for
from services.library import Library

app = Flask(__name__, template_folder='web/templates')
library = Library()

# Test için örnek veriler
library.add_book("Sefiller", "Victor Hugo", 1862)
library.add_book("Suç ve Ceza", "Dostoyevski", 1866)

@app.route('/')
def index():
    # HTML formundan gelen verileri alıyoruz
    search_term = request.args.get('search_term')
    search_type = request.args.get('search_type')
    
    books = library.books
    
    # Arama yapılmışsa filtreleme mantığı
    if search_term:
        search_term = search_term.lower()
        if search_type == 'author':
            # Yazara göre arama
            books = [b for b in books if search_term in b.author.lower()]
        else:
            # Varsayılan: Kitap adına göre arama
            books = [b for b in books if search_term in b.name.lower()]
        
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
