from flask import Flask, jsonify, request
from transformers import pipeline

# Initialize the text-generation pipeline
pipe = pipeline("text-generation", model="m42-health/Llama3-Med42-8B")

# Create Flask app
app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def hello():
    """Health check route."""
    return "<html><body><h1>API is running!</h1></body></html>"

@app.route('/generate', methods=['POST'])
def generate():
    """Route to handle text generation requests."""
    try:
        # Extract the input message from the request
        data = request.json
        if not data or 'messages' not in data:
            return jsonify({"error": "Invalid request format. 'messages' key is required."}), 400

        messages = data['messages']
        # Run the pipeline
        generated_text = pipe(data)

        return jsonify({"response": generated_text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    import os
    app.run()
