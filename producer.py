import random
from kafka import KafkaProducer
import time
from codec import encode_data

def generarTemperatura():
    return random.uniform(0, 110)

def generarHumedad():
    return random.randint(0, 100)

def generarDireccionViento():
    direcciones = ["N", "NE", "E", "SE", "S", "SO", "O", "NO"]
    return random.choice(direcciones)

# Configuraciones para el servidor
KAFKA_SERVER = 'lab9.alumchat.lol:9092'
TOPIC = '21700'

# Inicializar el Kafka Producer
producer = KafkaProducer(
    bootstrap_servers=KAFKA_SERVER
)

def enviarDatos():
    try:
        while True:
            # Generar los datos
            temperatura = generarTemperatura()
            humedad = generarHumedad()
            direccion_viento = generarDireccionViento()

            # Codificar los datos
            encoded_payload = encode_data(temperatura, humedad, direccion_viento)

            # Enviar los datos codificados al topic
            producer.send(TOPIC, value=encoded_payload)
            print(f"Datos enviados: temperatura={temperatura}, humedad={humedad}, direccion_viento={direccion_viento}")

            # Esperar entre 15 y 30 segundos
            tiempoEspera = random.uniform(5, 10)
            time.sleep(tiempoEspera)
    except KeyboardInterrupt:
        print("Envío de datos interrumpido manualmente.")

enviarDatos()
