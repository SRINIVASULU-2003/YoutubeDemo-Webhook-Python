from flask import Flask, request, jsonify
from gradio_client import Client, handle_file
import os

app = Flask(__name__)
if not os.path.exists("temp"):
        os.makedirs("temp")
# Initialize the Gradio client
client = Client("sitammeur/PicQ")

@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return jsonify({"error": "No image file found in the request"}), 400

    # Get the image file from the request
    image = request.files['image']
    
    # Save the file temporarily
    temp_path = os.path.join("temp", image.filename)
    image.save(temp_path)

    try:
        # Use the Gradio client to predict the result
        result = client.predict(
            image=handle_file(temp_path),
            question="extract the complete data from the image",
            api_name="/predict"
        )

        # Return the result as JSON
        return jsonify({"result": result})
    
    finally:
        # Clean up the temporary file
        if os.path.exists(temp_path):
            os.remove(temp_path)

