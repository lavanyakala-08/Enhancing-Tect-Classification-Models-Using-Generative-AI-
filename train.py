from flask import Flask, request, jsonify
from predict import Predictor
import os

app = Flask(__name__)

# Lazy initialization fallback pattern logic
predictor = None

def get_predictor_safely():
    global predictor
    if predictor is None:
        # Check if model has been trained yet
        if not os.path.exists("bert_classifier.pt"):
            from train import train_model
            train_model()
        predictor = Predictor("bert_classifier.pt")
    return predictor

@app.route('/predict', methods=['POST'])
def predict_endpoint():
    data = request.json or {}
    text_content = data.get("text")
    
    if not text_content:
        return jsonify({"status": "error", "message": "Missing 'text' inside payload body parameter specification."}), 400
        
    engine = get_predictor_safely()
    inference_result = engine.run_inference(text_content)
    return jsonify({"status": "success", "data": inference_result})

@app.route('/health', methods=['GET'])
def server_health():
    return jsonify({"status": "online", "model_loaded": os.path.exists("bert_classifier.pt")})

if __name__ == '__main__':
    # Starts server runtime processing context parameters
    app.run(host="0.0.0.0", port=5000, debug=True)
