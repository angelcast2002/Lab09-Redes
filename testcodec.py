from codec import encode_data, decode_data

# Datos de prueba
temperatura_original = 85.23
humedad_original = 45
direccion_viento_original = 'NE'

# Codificar los datos
payload = encode_data(temperatura_original, humedad_original, direccion_viento_original)

# Decodificar los datos
temperatura_decoded, humedad_decoded, direccion_viento_decoded = decode_data(payload)

# Imprimir los resultados
print("Datos Originales:")
print(f"Temperatura: {temperatura_original}")
print(f"Humedad: {humedad_original}")
print(f"Dirección del Viento: {direccion_viento_original}")

print("\nDatos Decodificados:")
print(f"Temperatura: {temperatura_decoded}")
print(f"Humedad: {humedad_decoded}")
print(f"Dirección del Viento: {direccion_viento_decoded}")
