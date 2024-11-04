# codec.py

direcciones_viento = ['N', 'NE', 'E', 'SE', 'S', 'SO', 'O', 'NO']
direcciones_map = {d: i for i, d in enumerate(direcciones_viento)}

def encode_data(temperatura, humedad, direccion_viento):
    temperatura_encoded = int((temperatura / 110) * (2**14 - 1))
    humedad_encoded = int(humedad)
    direccion_encoded = direcciones_map[direccion_viento]
    payload = (temperatura_encoded << 10) | (humedad_encoded << 3) | direccion_encoded
    return payload.to_bytes(3, 'big')

def decode_data(payload):
    data = int.from_bytes(payload, 'big')
    temperatura_encoded = (data >> 10) & 0x3FFF
    temperatura = (temperatura_encoded / (2**14 - 1)) * 110
    humedad_encoded = (data >> 3) & 0x7F
    direccion_encoded = data & 0x07
    direccion_viento = direcciones_viento[direccion_encoded]
    return temperatura, humedad_encoded, direccion_viento
