from flask import Flask, render_template, request
import json

app = Flask(__name__)

# Load fruit data from JSON file
with open('data/fruits.json') as f:
    fruit_data = json.load(f)

# Map hashes to box IDs
hash_to_box = {
    "a5d9ade08c608f8224bf0a5a0a3c13bb1cb3c9bff6fdb0cae77ca807b1ad3d6a": "box001",
    "d4c1ae9cf7f05de2fb0c2f78c10fd0be8d5e898b134cc69be124d75e2850e93c": "box002",
    "f1c9a4372a1e2dcdb97a36c9e89e1c9fc6c71d6cd81c135b1f406efaf2e71043": "box003",
    "9acdf0eb0e03221ef3e4f0b37870f89ac041d62b8f53d1be13d4e74c87b61aa4": "box004",
    "7c8b6e9f5a6f1d1c25e9b7b29e3b6e1f5e8e21bda7c6ef5a0b1c3d5e7f8a1f29": "box005"
}

@app.route('/product')
def product():
    hash_id = request.args.get('id')

    if not hash_id or hash_id not in hash_to_box:
        return "Invalid or missing product ID!", 404

    box_id = hash_to_box[hash_id]
    product_info = fruit_data.get(box_id)

    if not product_info:
        return "Product not found!", 404

    return render_template('product.html', box_id=box_id, product=product_info)

if __name__ == '__main__':
    app.run(debug=True)




