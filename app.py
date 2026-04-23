from flask import Flask, jsonify, request
import numpy as np
from sklearn.linear_model import LogisticRegression
import os

app = Flask(__name__)

# Train a very simple model on startup (avoids needing a separate .pkl file)
X = np.array([[1], [2], [3], [4]])
y = np.array([0, 0, 1, 1])
model = LogisticRegression()
model.fit(X, y)

@app.route('/')
def home():
    return jsonify({"message": "Classification API is running"})

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    if not data or 'val' not in data:
        return jsonify({"error": "Missing 'val' in request body"}), 400
    
    val = np.array([[data['val']]])
    prediction = int(model.predict(val)[0])
    return jsonify({"input": data['val'], "prediction": prediction})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)