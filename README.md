# ☀️ Clasificador de Fallas en Paneles Solares mediante Imágenes Infrarrojas

Este proyecto implementa una solución basada en visión por computadora para detectar **fallas térmicas** en paneles solares a partir de imágenes capturadas con cámaras infrarrojas. El sistema fue desarrollado como parte del **diplomado en Inteligencia Artificial** del programa **Samsung Innovation Campus** 2024.

---

## 📌 Objetivo

El propósito principal del proyecto es asistir en labores de mantenimiento predictivo y preventivo en instalaciones fotovoltaicas, permitiendo identificar **anomalías térmicas** mediante una red neuronal convolucional entrenada con imágenes reales.

---

## 🧰 Tecnologías Utilizadas

### 🧠 Machine Learning y Visión por Computador
- **Python 3.10**
- **TensorFlow / Keras** – Modelado de redes neuronales convolucionales (CNN)
- **OpenCV** – Carga y procesamiento de imágenes
- **scikit-learn** – Codificación de etiquetas y métricas
- **Pandas / NumPy** – Manipulación de datos
- **Matplotlib / Seaborn** – Visualización

### 🧪 Backend
- **FastAPI** – API REST para inferencia del modelo
- **Uvicorn** – Servidor ASGI

### 🎨 Frontend
- **ReactJS** – Interfaz de usuario
- **Axios** – Consumo de la API
- **Tailwind CSS** – Estilos

---

## 🧠 Descripción del Modelo

El modelo principal es una **Red Neuronal Convolucional (CNN)** construida desde cero. Se entrenó para clasificar imágenes térmicas de tamaño reducido (**40 x 24 píxeles**) en **dos clases**:

- `anómala` (falla presente)
- `normal` (sin anomalía)

### 🔢 Características del modelo:
- Número de capas: 3 convolucionales + 2 densas
- Función de activación: ReLU (ocultas), Softmax (salida)
- Regularización: Dropout y EarlyStopping
- Optimización: Adam
- Métrica: Accuracy
- Entrenamiento: 50+ épocas

### 🧪 Resultados:
- Precisión en entrenamiento: ~57%
- Precisión en validación: ~64%
> ⚠️ Indica presencia de **overfitting**, debido a conjunto de datos reducido y falta de normalización avanzada.

---

## 📂 Estructura del Proyecto

