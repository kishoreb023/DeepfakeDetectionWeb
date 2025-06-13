from flask import Flask, request, jsonify, render_template
from transformers import ViTImageProcessor, ViTForImageClassification
from PIL import Image
import torch
import os
from werkzeug.utils import secure_filename


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

MODEL_PATH = "DeepfakeDetectionWeb\deepfake_model"  
device = torch.device("cpu") 

model = ViTForImageClassification.from_pretrained(MODEL_PATH).to(device)
processor = ViTImageProcessor.from_pretrained(MODEL_PATH)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    try:
        # Save file
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        # Process image
        image = Image.open(file_path).convert("RGB")
        inputs = processor(images=image, return_tensors="pt").to(device)

        # Predict
        with torch.no_grad():
            outputs = model(**inputs)
            logits = outputs.logits
            predicted_idx = logits.argmax(-1).item()
            confidence = torch.nn.functional.softmax(logits, dim=-1)[0][predicted_idx].item() * 100
            label = model.config.id2label[predicted_idx]

        return jsonify({
    'prediction': label,
    'confidence': round(confidence, 2),
    'image_path': '/' + file_path.replace('\\', '/')
})


    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
