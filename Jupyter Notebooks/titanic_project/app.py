# Servidor FLASK
from flask import Flask, request, jsonify
import joblib
import numpy as np
import os

app = Flask(__name__)

# Cargar el modelo desde la carpeta 'models/'
model_path = os.path.join(os.path.dirname(__file__), 'models', 'svm_model.pkl')
model = joblib.load(model_path)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    features = np.array(data['features']).reshape(1, -1)
    prediction = model.predict(features)
    return jsonify({'prediction': int(prediction[0])})

if __name__ == '__main__':
    app.run(debug=True)