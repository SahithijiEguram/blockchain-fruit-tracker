from flask import Flask, render_template, request, redirect
import json

app = Flask(__name__)

# Load fruit data
with open('data/fruits.json') as f:
    fruit_data = json.load(f)

@app.route('/')
def home():
    return render_template('index.html')  # where QR and message shows

@app.route('/product')
def redirect_product():
    # Get hashed ID from QR
    hashed_id = request.args.get('id')
    
    # Example hardcoded mapping
    id_to_box = {
        "a5d9ade08c608f8224bf0a5a0a3c13bb1cb3c9bff6fdb0cae77ca807b1ad3d6a": "box001"
    }
    
    product_id = id_to_box.get(hashed_id)
    
    if product_id and product_id in fruit_data:
        return redirect(f'/product/{product_id}')
    else:
        return "Invalid or unknown product", 404

@app.route('/product/<product_id>')
def show_product(product_id):
    product = fruit_data.get(product_id)
    if product:
        return render_template('fruit_info.html', product=product, product_id=product_id)
    else:
        return "Product not found", 404

import os

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)


