from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def get_db():
    return sqlite3.connect('sportshop.db')

@app.route('/')
def home():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    conn.close()
    return render_template('products.html', products=products)

@app.route('/add', methods=['POST'])
def add():
    name = request.form['name']
    category = request.form['category']
    price = request.form['price']
    stock = request.form['stock']

    conn = get_db()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO products (name, category, price, stock) VALUES (?, ?, ?, ?)",
        (name, category, price, stock)
    )
    conn.commit()
    conn.close()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
