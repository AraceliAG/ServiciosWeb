import asyncio
import websockets

PORT = 6969
clientes = set()

async def websocket_handler(websocket, path):
    clientes.add(websocket)
    try:
        while True:
            try:
                message = await websocket.recv()
                await asyncio.gather(*[cliente.send(message) for cliente in clientes])
                if message == "exit":
                    break
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
