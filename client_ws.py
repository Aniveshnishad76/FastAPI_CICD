import asyncio
import websockets

async def hello():
    uri = "ws://localhost:8001/ws"
    async with websockets.connect(uri) as websocket:
        message = "Hello from FastAPI client!"
        await websocket.send(message)
        print(f"Sent message: {message}")
        response = await websocket.recv()
        print(f"Received response: {response}")

# Run the client
asyncio.run(hello())
