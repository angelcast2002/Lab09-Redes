import random
import json

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

for _ in range(5):
  mensaje = generarMensaje()
  print(mensaje)