import random
import time
import qrcode
import json
from hashlib import sha256

# Step 1: Simulate IoT Sensor Data Collection
def get_sensor_data():
    return {
        'fruit': 'Orange',
        'moisture': round(random.uniform(30, 70), 2),
        'temperature': round(random.uniform(20, 35), 2),
        'humidity': round(random.uniform(40, 80), 2),
        'pesticide_used': random.choice([True, False])
    }

# Step 2: Simulate Van Tracking Data
def get_van_tracking_data():
    return {
        'vehicle_temperature': round(random.uniform(18, 25), 2),
        'current_location': '17.385044, 78.486671',  # Hyderabad
        'retail_shop': 'ABC Fruits Retailer, Hyderabad'
    }

# Step 3: Upload to Simulated Blockchain (Hash)
def upload_to_blockchain(data):
    data_str = str(data)
    hash_val = sha256(data_str.encode()).hexdigest()
    return hash_val

# Step 4: Generate QR Code
def generate_qr(data_dict, blockchain_hash):
    full_payload = {
        'blockchain_hash': blockchain_hash,
        'trace_details': data_dict
    }

    qr_data = json.dumps(full_payload, indent=2)

    # Generate high-quality QR
    qr = qrcode.QRCode(
        version=2,
        box_size=10,
        border=4
    )
    qr.add_data(qr_data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    img.save("fruit_box_qrcode.png")
    print("\n✅ QR Code saved as 'fruit_box_qrcode.png'")
    print("📦 Print or paste this on the fruit box. Scannable from any camera 📲")

# Main Flow
if __name__ == "__main__":
    print("🍊 Starting QR generation for Fruit Box")

    sensor_data = get_sensor_data()
    van_data = get_van_tracking_data()
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')

    combined_data = {
        'sensor_data': sensor_data,
        'van_tracking': van_data,
        'timestamp': timestamp
    }

    # Upload to blockchain
    blockchain_hash = upload_to_blockchain(combined_data)

    # Generate QR Code
    generate_qr(combined_data, blockchain_hash)
