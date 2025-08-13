from flask import Flask, request, jsonify, render_template
import os
from flask_cors import CORS, cross_origin
from cnnClassfier.utils.common import decodeImage  # ✅ check spelling!
from cnnClassfier.pipeline.prediction import PredictionPipeline

os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)
CORS(app)

class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"
        self.classifier = PredictionPipeline(self.filename)

# ✅ Initialize here so it exists for all runs
clApp = ClientApp()

@app.route("/", methods=['GET'])
@cross_origin()
def home():
    return render_template('index.html')

@app.route("/train", methods=['GET', 'POST'])
@cross_origin()
def trainRoute():
    os.system("python main.py")
    return "Training done successfully!"

@app.route("/predict", methods=['POST'])
@cross_origin()
def predictRoute():
    try:
        image = request.json['image']  # Expecting Base64 string from frontend
        decodeImage(image, clApp.filename)
        result = clApp.classifier.predict()
        return jsonify(result)
    except Exception as e:
        import traceback
        traceback.print_exc()  # 🔹 This will print the full error in the terminal
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
