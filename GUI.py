import asyncio
import websockets
from sys import exit

class Communicator:
    def __init__(self, websocket):
        self.websocket = websocket
 
    async def handle_message(message, websocket):
        print("Received message: ", message)


    async def send_message(self, message):
        await self.websocket.send(message)



async def server(websocket, path):
    global communicator
    communicator = Communicator(websocket)
    try:
        while True:
            await communicator.send_message("Hello from Python!")
            message = await websocket.recv()
            await communicator.handle_message(message, websocket)
    except:
        exit()


if __name__ == '__main__':
    start_server = websockets.serve(server, 'localhost', 8000)
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()