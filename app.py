from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

# Crear una base de datos SQLite y poblarla con datos de ejemplo
conn = sqlite3.connect('products.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        price REAL NOT NULL,
        description TEXT NOT NULL
    )
''')
cursor.execute("INSERT INTO products (name, price, description) VALUES (?, ?, ?)", ('Producto A', 19.99, 'Este es el producto A'))
cursor.execute("INSERT INTO products (name, price, description) VALUES (?, ?, ?)", ('Producto B', 29.99, 'Este es el producto B'))
conn.commit()
conn.close()

# Definir la ruta para mostrar los productos
@app.route('/')
def index():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('SELECT name, price, description FROM products')
    products = cursor.fetchall()
    conn.close()
    return render_template('index.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)