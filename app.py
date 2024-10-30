from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Key for managing sessions (required for cart)

# Sample product data
products = [
    {"id": 1, "name": "Lipstick", "price": 20.00, "description": "Red lipstick", "image": "lipstick.jpg"},
    {"id": 2, "name": "Foundation", "price": 35.00, "description": "Natural foundation", "image": "foundation.jpg"},
    {"id": 3, "name": "Mascara", "price": 15.00, "description": "Waterproof mascara", "image": "mascara.jpg"}
]

# Route for homepage
@app.route('/')
def index():
    return render_template('index.html', products=products)

# Route for product page
@app.route('/product/<int:product_id>')
def product(product_id):
    prod = next((item for item in products if item["id"] == product_id), None)
    return render_template('product.html', product=prod)

# Route to add product to cart
@app.route('/add_to_cart/<int:product_id>')
def add_to_cart(product_id):
    if 'cart' not in session:
        session['cart'] = []
    session['cart'].append(product_id)
    return redirect(url_for('cart'))

# Route for cart page
@app.route('/cart')
def cart():
    cart_items = [p for p in products if p["id"] in session.get('cart', [])]
    total_price = sum(item['price'] for item in cart_items)
    return render_template('cart.html', cart=cart_items, total=total_price)

# Route to clear the cart
@app.route('/clear_cart')
def clear_cart():
    session.pop('cart', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
