import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './App.css'; // Para los estilos CSS personalizados

function App() {
  const [selectedFile, setSelectedFile] = useState(null);
  const [preview, setPreview] = useState(null);
  const [prediction, setPrediction] = useState('');

  const handleFileChange = (event) => {
    const file = event.target.files[0];
    setSelectedFile(file);
    setPreview(URL.createObjectURL(file));
    setPrediction('');  // Limpiar la predicción anterior
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    const formData = new FormData();
    formData.append('file', selectedFile);

    try {
      const response = await axios.post('https://modulsdespliegue.onrender.com/predict/', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });
      setPrediction(response.data.prediction);
    } catch (error) {
      console.error('Error uploading the file', error);
    }
  };

  // Script de keep-alive
  useEffect(() => {
    const interval = setInterval(() => {
      axios.get('https://modulsfrontend.onrender.com/')
        .then(response => console.log('Manteniendo la página activa'))
        .catch(error => console.error('Error al enviar keep-alive', error));
    }, 40000); // Enviar cada 60 segundos

    return () => clearInterval(interval);
    
  }, []);
  
  return (
    <div className="App">
      <header className="App-header">
        <img src="https://i.imgur.com/F8UzITO.png" alt="logo" className="logo" />
        <h1>scopeGenius</h1>
        <form onSubmit={handleSubmit} className="form">
          <label className="file-label">
            Choose File
            <input type="file" onChange={handleFileChange} className="file-input" />
          </label>
          <button type="submit" className="submit-Ñbutton">Upload and Predict</button>
        </form>
        {preview && <img src={preview} alt="preview" className="image-preview" />}
        {prediction && <h2 className="prediction">Prediction: {prediction}</h2>}
      </header>
    </div>
  );
}

export default App;
