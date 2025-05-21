import face_recognition
import base64
import json
import paho.mqtt.client as mqtt
from utils import decode_image

known_image = face_recognition.load_image_file("autorizado.jpg")
known_encoding = face_recognition.face_encodings(known_image)[0]

def on_connect(client, userdata, flags, rc):
    print("✅ Conectado a MQTT")
    client.subscribe("imagen/entrada")

def on_message(client, userdata, msg):
    print("📥 Imagen recibida")
    data = json.loads(msg.payload.decode())
    image = decode_image(data['image'])
    faces = face_recognition.face_encodings(image)
    if faces:
        match = face_recognition.compare_faces([known_encoding], faces[0])[0]
        print("🔐 AUTORIZADO ✅" if match else "❌ DENEGADO")
    else:
        print("🚫 No se detectó rostro")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("localhost", 1883, 60)
client.loop_forever()