import asyncio
import websockets


async def client():
    uri = "ws://localhost:8765"
    async  with websockets.connect(uri) as websocket:
        message = "Привет, сервер!"  # Сообщение, которое отправит клиент
        print(f"Отправка: {message}")
        await websocket.send(message)  # Отправляем сообщение
        for _ in range(1,6):
            response = await websocket.recv()
            print(f"{_} Ответ от сервера: {response}")


asyncio.run(client())
