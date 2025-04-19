import qrcode

# This is the LIVE Render URL pointing to box001's product page
url = "https://blockchain-fruit-tracker.onrender.com/product/box001"

# Create QR Code
qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=5
)
qr.add_data(url)
qr.make(fit=True)

# Save the QR code image
img = qr.make_image(fill_color="black", back_color="white")
img.save("static/fruit_trace_qr.png")

print("✅ QR code generated linking to:", url)
print("📍 Saved as 'static/fruit_trace_qr.png'")
