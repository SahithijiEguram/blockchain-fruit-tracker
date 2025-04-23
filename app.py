from flask import Flask, render_template, send_from_directory
import json
import os

app = Flask(__name__)

# Load data from JSON
with open('data/fruits.json') as f:
    fruits_data = json.load(f)

# Route for viewing product details
@app.route('/product/<box_id>', methods=['GET'])
def product_by_box(box_id):
    print(f"Received request for box_id: {box_id}")
    info = fruits_data.get(box_id)
    if not info:
        print("No data found.")
        return "No data found for this box ID", 404
    print("Rendering fruit_info.html")
    return render_template('fruit_info.html', box_id=box_id, info=info)

# Optional: route to serve static files like QR images
@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory('static', filename)

# For local testing
if __name__ == '__main__':
    app.run(debug=True)
