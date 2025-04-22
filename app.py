from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

# Load the data once at the top
with open('data/fruits.json') as f:
    fruits_data = json.load(f)

# Mapping of hash to box ID
hash_to_box = {
    "a5d9ade08c608f8224bf0a5a0a3c13bb1cb3c9bff6fdb0cae77ca807b1ad3d6a": "box001",
    "another_hash": "box002",
    # add the rest
}

@app.route('/product')
def product():
    hash_val = request.args.get('id')
    box_id = hash_to_box.get(hash_val)

    if not box_id:
        return "Invalid or unknown hash!", 404

    info = fruits_data.get(box_id)

    if not info:
        return "No data found for this box ID", 404

    return render_template('fruit_info.html', box_id=box_id, info=info)

if __name__ == '__main__':
    app.run(debug=True)




