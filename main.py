import json
import asyncio
from websockets.asyncio.server import serve
from game.board import pieces


clients = []

async def onConnected(ws):
    global clients

    clients.append(ws)

    await ws.send(json.dumps({"type": "message", "value": "send: Привет"}))
    await ws.send(json.dumps({"type": "pieces", "value": pieces}))

    async for text in ws:
        print(f"Received: {text}")
        for client in clients:
            await client.send(f"Send: {text}")

async def main():
    async with serve(onConnected, "localhost", 8765) as server:
        await server.serve_forever()

if __name__ == "__main__":
    asyncio.run(main())