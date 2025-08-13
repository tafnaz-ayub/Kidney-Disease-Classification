import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os
import random

class PredictionPipeline:
    def __init__(self, filename):
        self.filename = filename

    def predict(self):
        # Load model
        model = load_model(os.path.join("model", "model.h5"))

        # Prepare image
        test_image = image.load_img(self.filename, target_size=(224, 224))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)
        test_image = test_image / 255.0  # normalize if model trained with normalization

        # Make prediction
        result = np.argmax(model.predict(test_image), axis=1)

        # Mapping index to class name
        class_labels = ['Cyst', 'Normal', 'Stone', 'Tumor']
        prediction = class_labels[result[0]]

        # Funny & healthy messages
        funny_messages = {
            "Cyst": [
                "We found a cyst – it’s just squatting rent-free, nothing serious.",
                "Cyst spotted! More of a lazy bubble than a troublemaker.",
                "Diagnosis: cyst. Treatment: a good laugh and a cup of tea.",
                "A cyst showed up – probably just photobombing your scan."
            ],
            "Normal": [
                "All clear! Your kidneys are basically the rockstars of filtration.",
                "Nothing to see here – your kidneys are just chilling.",
                "Kidneys status: perfect! Hydration is their love language.",
                "Everything’s normal – keep up the healthy habits!"
            ],
            "Stone": [
                "Uh-oh, a kidney stone! Small but mighty… and not in a good way.",
                "Stone detected – it’s not a diamond, so let’s get rid of it.",
                "Looks like a kidney stone snuck in. Time to evict it!",
                "Stone spotted! Unfortunately, not the collectible kind."
            ],
            "Tumor": [
                "A tumor showed up – but remember, not all tumors are villains.",
                "We found a tumor – let's get it checked, just to be safe.",
                "Tumor detected – time for your medical team to show off their skills.",
                "This tumor thinks it’s important… your doctor will set it straight."
            ]
        }

        # Pick a random funny message for the prediction
        message = random.choice(funny_messages[prediction])

        # Return both prediction and message
        return [{"image": prediction, "message": message}]