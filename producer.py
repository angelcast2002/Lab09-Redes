import random
import json
from kafka import KafkaProducer
import time

def generarTemperatura():
  return round(random.uniform(0, 110), 2)

def generarHumedad():
  return random.randint(0, 100)

def generarDireccionViento():
  direcciones = ["N", "NO", "O", "SO", "S", "SE", "E", "NE"]
  return random.choice(direcciones)

def generarMensaje():
  datos = {
    "temperatura": generarTemperatura(),
    "humedad": generarHumedad(),
    "direccionViento": generarDireccionViento()
  }
  return json.dumps(datos)

# Configuraciones para el servidor
KAFKA_SERVER = 'lab9.alumchat.lol:9092'
TOPIC = '21700'

# Inicializar el Kafka Producer
producer = KafkaProducer(
  bootstrap_servers=KAFKA_SERVER,
  value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def enviarDatos():
  try:
    while True:
      # Generar el mensaje
      mensaje = json.loads(generarMensaje())
      
      # Enviar los datos al topic
      producer.send(TOPIC, value=mensaje)
      print(f"Datos enviados: {mensaje}")
      
      # Hacer un sleep de 15 a 30 segundos
      tiempoEspera = random.uniform(15, 30)
      time.sleep(tiempoEspera)
  except KeyboardInterrupt:
    print("Envío de datos interrumpido manualmente.")
    
enviarDatos()