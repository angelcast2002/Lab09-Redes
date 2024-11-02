from kafka import KafkaConsumer
import json
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Inicializar listas para almacenar datos

allTemp = []
allHume = []
allWind = []

# Configuraciones para el servidor
KAFKA_SERVER = 'lab9.alumchat.lol:9092'
TOPIC = '21700'

# Inicializar el Kafka consumer
consumer = KafkaConsumer(
  TOPIC,
  group_id='foo2',
  bootstrap_servers=KAFKA_SERVER,
  value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

# Configurar la figura de matplotlib
fig, (ax_temp, ax_hume, ax_wind) = plt.subplots(3, 1, figsize=(6, 6))
fig.tight_layout(pad=3.0)

# Función para actualizar las gráficas
def actualizar(frame):
    try:
        # Recibir un mensaje del Kafka Consumer
        mensaje = next(consumer)
        payload = mensaje.value
        allTemp.append(payload['temperatura'])
        allHume.append(payload['humedad'])
        allWind.append(payload['direccionViento'])

        # Limitar la cantidad de datos mostrados (por ejemplo, últimos 50)
        if len(allTemp) > 50:
            allTemp.pop(0)
            allHume.pop(0)
            allWind.pop(0)

        # Actualizar las gráficas
        ax_temp.clear()
        ax_temp.plot(allTemp, label="Temperatura", color="red")
        ax_temp.set_ylabel("°C")
        ax_temp.legend()

        ax_hume.clear()
        ax_hume.plot(allHume, label="Humedad", color="blue")
        ax_hume.set_ylabel("%")
        ax_hume.legend()

        ax_wind.clear()
        ax_wind.plot(allWind, label="Dirección del Viento", color="green")
        ax_wind.set_ylabel("Dirección")
        ax_wind.legend()
    except StopIteration:
        pass

# Configurar la animación
ani = FuncAnimation(fig, actualizar, interval=1000)

# Mostrar la gráfica
plt.show()
