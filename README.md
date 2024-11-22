# 🌱 **MINIPROYECTO 3: Reconocimiento de Patógenos en Plantas con TinyML en Raspberry Pi**  

---

## 📝 **Resumen**  
Este proyecto desarrolla un sistema **TinyML** para el reconocimiento de patógenos en plantas, ejecutado en una **Raspberry Pi** con una cámara USB. Utilizando redes neuronales convolucionales (CNN) preentrenadas y optimizadas con TensorFlow Lite, permite la identificación de enfermedades vegetales en tiempo real. Esta solución es una herramienta accesible y sostenible para la detección temprana de enfermedades, promoviendo la **agricultura sostenible**.  

---

## 🎯 **Objetivos**  
### 🏆 **Objetivo General**  
Desarrollar un sistema basado en **TinyML** para reconocer patógenos en plantas con una **Raspberry Pi 4** y una cámara USB, facilitando decisiones rápidas en **agricultura sostenible**. Las imágenes con las que se realizó el entrenamiento de la red de encuentran en el enlace de abajo.

[🔗Plant Pathogens Dataset - Kaggle](https://www.kaggle.com/datasets/sujallimje/plant-pathogens) 

### ✅ **Objetivos Específicos**  
1. 🧠 Entrenar un modelo **CNN** preentrenado (**MobileNetV2**) en Google Colab.  
2. ⚡ Optimizar el modelo con TensorFlow Lite para uso en dispositivos de borde.  
3. 📸 Integrar la captura de imágenes en tiempo real con una cámara USB.  
4. 🚨 Diseñar un sistema de alertas visuales/sonoras para notificar detecciones.  
5. 🔬 Validar el desempeño en campo, midiendo precisión y eficiencia.  

---

## 🛠️ **Metodología**  
 
### 1️⃣ **Preparación del Dataset**  
📂 Datos de **Kaggle** con imágenes de hojas clasificadas en:  
- 🌿 Healthy  
- 🦠 Bacteria  
- 🍄 Fungus  

🔄 **Procesamiento**:  
- Normalización de imágenes a `128x128 px`.  
- Dividido en 80% entrenamiento y 20% testeo.  

### 2️⃣ **Entrenamiento del Modelo**  
💻 **Google Colab**:  
- Modelo base: **MobileNetV2** (preentrenado en ImageNet).  
- Optimización: Ajuste de hiperparámetros para balancear **precisión** y **velocidad**.  

### 3️⃣ **Optimización para Edge Computing**  
📉 Conversión del modelo a **TensorFlow Lite** con cuantización para reducir tamaño y mejorar la inferencia en la Raspberry Pi.  

### 4️⃣ **Configuración del Hardware**  
- **Hardware:**  
  - 🔴 **Raspberry Pi 4**  
  - 📷 **Cámara USB**  
  - 🛠️ Actuadores: LED, buzzer, servomotor, relés.  

- **Software:**  
  - 📦 **OpenCV** para captura y procesamiento de imágenes.  
  - 📜 Scripts en Python para inferencias y control de actuadores.  

### 5️⃣ **Sistema de Alertas**  
- 🚦 **Healthy:** LED verde.  
- 🚨 **Bacteria:** Buzzer + LED rojo.  
- 🚿 **Fungus:** Activación de servomotor.  

### 6️⃣ **Validación en Campo**  
🔍 Evaluación en **entornos reales**:  
- Precisión ≈ **94%**.  
- Consumo energético.  
- Respuesta de los actuadores.  

---

## 📊 **Resultados**  
### ✔️ **Clasificación Exitosa:**  
El sistema distingue entre `Healthy`, `Bacteria`, y `Fungus` con alta precisión.  

### 🔔 **Alertas Visuales y Sonoras:**  
- 🌿 **Healthy:** LED verde.  
- 🦠 **Bacteria:** Buzzer + LED rojo.  
- 🍄 **Fungus:** Activación de servomotor.  

### 💡 **Implementación Real en Campo:**  
El sistema demuestra su eficacia en condiciones reales, apoyando la **agricultura sostenible**.  

---

## 🔧 **Requisitos Técnicos**  
### 🖥️ **Hardware:**  
- **Raspberry Pi 4** (o superior).  
- Cámara USB compatible.  
- Actuadores: LEDs, buzzer, servomotor, relés.  

### 📦 **Dependencias:**  
```bash
pip install tensorflow opencv-python-headless gpiozero
