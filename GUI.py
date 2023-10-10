import asyncio
import websockets
import threading
import functions
from sys import exit

### Unless absolutely necessary DO NOT CHANGE this file ###
### Only the handler may be changed, but I suggest outsourcing work to another file. ###

class Communicator:
    def __init__(self):
        self.is_ready = False

    def set_websocket(self, websocket):
        self.websocket = websocket
        self.is_ready = True
 
    async def handle_message(self, message):
        ### Handle messages from java here ###
        try:
            type = int(message[0:4])
        except ValueError:
            print("Incoreect header for message")
        message = message[5:]
        if type == 0:
            print("Debug: " + message)
        elif type == 100:
            # process random information
            pass
        elif type == 200:
            print("ISAAC received input: " + message)
            threading.Thread(target=functions.query_handler, args=message, daemon=True)
        else:
            print("Code not implemented yet")



    async def send_message(self, message):
        await self.websocket.send(message)



async def server(websocket, path):
    communicator.set_websocket(websocket)
    try:
        while True:
            message = await websocket.recv()
            await communicator.handle_message(message)
    except:
        exit()


def GUI_main():
    start_server = websockets.serve(server, 'localhost', 8000)
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()


def start_GUI_loop():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(GUI_main())


communicator = Communicator()
if __name__ == '__main__':
    GUI_main()