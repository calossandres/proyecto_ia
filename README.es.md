# Sistema de Visión por Computador en Tiempo Real con MQTT

Este proyecto implementa un módulo de inteligencia artificial para visión por computador que opera en tiempo real, diseñado para integrarse en sistemas IoT distribuidos mediante el protocolo MQTT.

El sistema recibe imágenes desde dispositivos externos (por ejemplo, ESP32, cámaras IP u otros módulos del sistema), procesa la información visual y genera decisiones automáticas basadas en reconocimiento facial y detección de objetos.

# Objetivo del Proyecto

Desarrollar un servicio de inferencia de IA desacoplado, capaz de:

Recibir imágenes en tiempo real mediante MQTT

Verificar si un rostro está autorizado o no

Detectar objetos relevantes (personas y animales)

Funcionar como módulo independiente dentro de una arquitectura IoT

Este enfoque permite que el sistema escale fácilmente y se integre con otros componentes sin acoplamiento directo.

# Funcionalidades Principales

## Reconocimiento Facial

Se utiliza la librería face_recognition para extraer embeddings faciales.

Se compara la imagen recibida con un rostro previamente autorizado.

El sistema devuelve:

✅ AUTORIZADO si el rostro coincide

❌ DENEGADO si no coincide o no se detecta rostro

# Detección de Objetos (YOLOv8)

Se integra el modelo YOLOv8 para detección de objetos en imágenes.

Se identifican clases específicas como:

person

dog

Se reportan las detecciones junto con su nivel de confianza.

# Comunicación por MQTT

El sistema actúa como cliente suscriptor MQTT.

Recibe imágenes codificadas en Base64 desde un tópico definido.

# Puede integrarse fácilmente con:

Dispositivos embebidos (ESP32)

Otros servicios backend

Sistemas de almacenamiento como MongoDB/GridFS



# Estructura del Proyecto
├── recibidor_mqtt.py      # Servicio principal de IA (suscriptor MQTT)
├── publicador.py          # Cliente de prueba que envía imágenes
├── utils.py               # Utilidades para codificar/decodificar imágenes
├── prueba.jpg             # Imagen del rostro autorizado
├── yolov8n.pt             # Modelo YOLOv8 preentrenado
├── requirements.txt       # Dependencias del proyecto
└── README.md

# Tecnologías Utilizadas

Python

MQTT (Mosquitto)

face_recognition / dlib

OpenCV

YOLOv8 (Ultralytics)

NumPy

# Cómo Ejecutar el Proyecto en Local
1️.Iniciar el broker MQTT
mosquitto

2️.Instalar dependencias
pip install -r requirements.txt

3️. Ejecutar el módulo de IA
python recibidor_mqtt.py


El sistema quedará a la espera de imágenes entrantes.

4️.Enviar una imagen de prueba
python publicador.py

## Resultado Esperado

En la consola del módulo IA se mostrarán mensajes como:

🔐 AUTORIZADO ✅

❌ DENEGADO

🟢 Detectado: person (0.98)

⚠️ No se detectaron objetos relevantes


# Rol y Aporte Personal

En este proyecto fui responsable de:

Diseño del módulo de inferencia de IA

Implementación del reconocimiento facial

Integración de YOLOv8 para detección de objetos

Comunicación en tiempo real mediante MQTT

Desarrollo de un sistema desacoplado y reutilizable
