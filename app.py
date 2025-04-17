from flask import Flask, render_template, request
import json

app = Flask(__name__)

# Map hashed IDs to box IDs
hash_map = {
    "a5d9ade08c608f8224bf0a5a0a3c13bb1cb3c9bff6fdb0cae77ca807b1ad3d6a": "box001",
    # Add more mappings as needed
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/product')
def product():
    product_hash = request.args.get('id')
    box_id = hash_map.get(product_hash)

    if not box_id:
        return "Invalid or unknown product ID", 404

    with open('data/fruits.json') as f:
        data = json.load(f)

    product_data = data.get(box_id)
    if not product_data:
        return "Product data not found", 404

    return render_template('fruit_info.html', product=product_data)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)


