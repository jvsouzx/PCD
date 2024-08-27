import asyncio
import websockets

connectet_clients = set()

async def handle_client(websocket, path):
    connectet_clients.add(websocket)
    try:
        async for message in websocket:
            for client in connectet_clients:
                if client != websocket:
                    await client.send(message)
    finally:
        connectet_clients.remove(websocket)

async def main():
    async with websockets.serve(handle_client, "localhost", 8765):
        await asyncio.Future()

asyncio.run(main())