from flask import Flask, render_template, request, send_from_directory
import json
import os

app = Flask(__name__)

# Load fruit data
with open('data/fruits.json', 'r') as f:
    fruits_data = json.load(f)

# Route to show homepage with QR code
@app.route('/')
def index():
    return render_template('index.html')  # This page will show the QR code image

# Route to serve product by box ID (for QR link like /product/box001)
@app.route('/product/<box_id>')
def product_by_box(box_id):
    info = fruits_data.get(box_id)
    if not info:
        return "No data found for this box ID", 404
    return render_template('fruit_info.html', box_id=box_id, info=info)

# Optional: to serve QR image from static folder
@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory('static', filename)

if __name__ == '__main__':
    app.run(debug=True)
