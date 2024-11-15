import logging

import uvicorn
from fastapi import FastAPI, Depends
from starlette.middleware.cors import CORSMiddleware
from starlette.websockets import WebSocket
from middleware import CustomMiddleware

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Adjust this as needed
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ["*"],  # Allow all headers
)
app.add_middleware(CustomMiddleware, paths=["/"])
@app.get("/")
async def read_root():
    return {
        "message": "Success",
        "data": [
            {
                "id": 1,
                "name": "Some Description",
                "category": "men",
                "image": "/home/neosoft/fastapi/Assets/men.jpeg",
                "discounted_price": 100,
                "original_price": 150,
            },
            {
                "id": 2,
                "name": "Some Description",
                "category": "men",
                "image": "/home/neosoft/fastapi/Assets/men1.jpeg",
                "discounted_price": 900,
                "original_price":1000,
            },
            {
                "id": 3,
                "name": "Some Description",
                "category": "men",
                "image": "/home/neosoft/fastapi/Assets/men2.jpeg",
                "discounted_price": 300,
                "original_price": 5000,
            },
            {
                "id": 4,
                "name": "Some Description",
                "category": "men",
                "image": "/home/neosoft/fastapi/Assets/men3.jpeg",
                "discounted_price": 800,
                "original_price": 1000,
            },
            {
                "id": 5,
                "name": "Some Description",
                "category": "women",
                "image": "/home/neosoft/fastapi/Assets/female.jpeg",
                "discounted_price": 900,
                "original_price": 1000,
            },
            {
                "id": 6,
                "name": "Some Description",
                "category": "women",
                "image": "/home/neosoft/fastapi/Assets/female1.jpeg",
                "discounted_price": 1900,
                "original_price": 11000,
            },
            {
                "id": 7,
                "name": "Some Description",
                "category": "women",
                "image": "/home/neosoft/fastapi/Assets/female2.jpeg",
                "discounted_price": 1200,
                "original_price": 12000,
            },
            {
                "id": 8,
                "name": "Some Description",
                "category": "women",
                "image": "/home/neosoft/fastapi/Assets/female3.jpeg",
                "discounted_price": 11200,
                "original_price": 123000,
            },
            {
                "id": 9,
                "name": "Some Description",
                "category": "women",
                "image": "/home/neosoft/fastapi/Assets/female4.jpeg",
                "discounted_price": 12000,
                "original_price": 120000,
            },
            {
                "id": 10,
                "name": "Some Description",
                "category": "kid",
                "image": "/home/neosoft/fastapi/Assets/kid1.jpeg",
                "discounted_price": 800,
                "original_price": 1000,
            },
            {
                "id": 11,
                "name": "Some Description",
                "category": "kid",
                "image": "/home/neosoft/fastapi/Assets/kid2.jpeg",
                "discounted_price": 200,
                "original_price": 500,
            },
            {
                "id": 12,
                "name": "Some Description",
                "category": "kid",
                "image": "/home/neosoft/fastapi/Assets/kid3.jpeg",
                "discounted_price": 800,
                "original_price": 1000,
            },
            {
                "id": 13,
                "name": "Some Description",
                "category": "kid",
                "image": "/home/neosoft/fastapi/Assets/kid4.jpeg",
                "discounted_price": 700,
                "original_price": 900,
            },
        ]
    }

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "query": q}


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            message = await websocket.receive_text()
            print("Received Message: ", message)
            await websocket.send_text(message)
    except Exception as e:
        print(e)
    finally:
        await websocket.close()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)

