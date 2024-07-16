from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from keras.models import load_model
from PIL import Image
import numpy as np
import pickle

app = FastAPI()

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Permite solicitudes desde esta URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Cargar el modelo de Keras
model = load_model(r'backend/model_066.h5')

# Cargar el LabelEncoder
with open(r'backend/label_encoder.pkl', 'rb') as file:
    encoder = pickle.load(file)

@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
    try:
        image = Image.open(file.file).convert('L')
        image = image.resize((40, 24))
        input_data = np.array(image).reshape(1, 40, 24, 1).astype(np.float32) / 255.0
        prediction = model.predict(input_data)
        predicted_class = np.argmax(prediction)
        predicted_label = encoder.inverse_transform([predicted_class])[0]
        
        return {"prediction": predicted_label}
    except Exception as e:
        return {"error": str(e)}
