from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from keras.models import load_model
from PIL import Image
import numpy as np
import pickle
import os

app = FastAPI()


# Configurar CORS para HTTP
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://modulsfrontend.onrender.com"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configurar CORS para WebSockets
app.add_middleware(WebSocketMiddleware, allow_origins=["https://modulsfrontend.onrender.com"])

# Verifica la ruta actual
print(os.getcwd())

# Intenta abrir el modelo
model_path = 'model_066.h5'
if os.path.exists(model_path):
    print(f"El archivo {model_path} existe.")
    # Cargar el modelo
    model = load_model(model_path)
else:
    print(f"No se pudo encontrar el archivo {model_path}.")

# Verifica la ruta actual
print(os.getcwd())

# Intenta abrir el archivo label_encoder.pkl
label_encoder_path = 'label_encoder.pkl'
if os.path.exists(label_encoder_path):
    print(f"El archivo {label_encoder_path} existe.")
    # Cargar el LabelEncoder
    with open(label_encoder_path, 'rb') as file:
        encoder = pickle.load(file)
else:
    print(f"No se pudo encontrar el archivo {label_encoder_path}.")


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
