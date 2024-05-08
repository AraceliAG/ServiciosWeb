import asyncio
import websockets
import json  # Agregar esta línea

PORT = 6969
clientes = set()

async def websocket_handler(websocket, path):
    clientes.add(websocket)
    try:
        while True:
            try:
                message = await websocket.recv()
                if message == "exit":
                    break
                else:
                    # Convertir el mensaje JSON a un diccionario de Python
                    datos = json.loads(message)
                    
                    # Realizar la suma de los valores recibidos
                    suma_total = sum(datos.values())
                    
                    # Convertir el resultado de la suma a un mensaje JSON
                    resultado_suma = json.dumps({"suma_total": suma_total})
                    
                    # Enviar el resultado de vuelta a todos los clientes conectados
                    await asyncio.gather(*[cliente.send(resultado_suma) for cliente in clientes])
            except websockets.ConnectionClosed:
                break
    finally:
        clientes.remove(websocket)

async def start_websocket_server():
    async with websockets.serve(websocket_handler, "localhost", PORT):
        print(f"Servidor WebSocket iniciado correctamente.")
        await asyncio.Future()

def run_server():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(start_websocket_server())

if __name__ == "__main__":
    run_server()
