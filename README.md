# Deepfake Detection Web App

This project is a Flask-based web application for detecting deepfake images using a custom-trained deep learning model. The system provides an intuitive UI where users can upload an image, and it instantly predicts whether the image is **Real** or **Fake**, along with a confidence score and a visual confidence bar.

---

## 🚀 Features

- 🖼️ Upload any facial image (JPEG/PNG)
- 🤖 Predicts whether the image is a **Deepfake (Fake)** or **Real**
- 📊 Displays confidence score with a matching bar chart
- 🧠 Uses a custom-trained deep learning model for accurate detection
- ⚡ Fast, interactive, and mobile-friendly user interface
- 🎨 Animated, modern frontend built with HTML, CSS, and JavaScript

---

## 🛠️ Technologies Used

- Python (Flask)
- TensorFlow / Keras
- HTML5, CSS3, JavaScript
- Bootstrap (for UI responsiveness)
- Matplotlib (for bar chart rendering)

---

## 📁 Project Structure

DeepfakeDetectionWeb/
├── app.py # Main Flask application
├── model/ # Trained model files
├── static/
│ ├── style.css # Custom styling
│ └── uploads/ # Stores uploaded images temporarily
├── templates/
│ └── index.html # Frontend HTML page
└── README.md


---

## 🧪 How to Run Locally

1. Clone the repo:
git clone https://github.com/kishoreb023/DeepfakeDetectionWeb.git
cd DeepfakeDetectionWeb

2. Install dependencies:
pip install -r requirements.txt


3. Place your trained model in the `model/` folder.

4. Run the app:
python app.py

5. Visit [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

---

## 📸 Sample Prediction Output

- Prediction: **Fake**
- Confidence: **98.45%**
- ![Sample Image](static/sample_output.png)

---

## 📌 Note

- This project uses a **custom-trained model**, not pre-trained ViT or external APIs.
- Compatible with CPU-based inference (no GPU required).
- Designed for educational and research purposes.

---

## 🙌 Acknowledgements

Thanks to open-source contributors and deepfake research datasets used during model training.

---

## 📬 Contact

For inquiries or collaborations:  
📧 kishoread023@gmail.com  
🌐 [LinkedIn](https://www.linkedin.com/in/kishoreb023)
