import websockets
import asyncio

async def cliente():
    try:
        websocket = await websockets.connect("ws://localhost:6969", ping_interval=None)
        while True:
            mensaje = input("Introduce el mensaje: ")
            await websocket.send(mensaje)
            msg = await websocket.recv()
            print("Se recibió el mensaje: ", msg)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(cliente())
