from GUI import *
import threading
from time import sleep


if __name__ == '__main__':
    GUI_thread = threading.Thread(target=start_GUI_loop, daemon=True)
    GUI_thread.start()
    while (True):
        sleep(10)
        if communicator.is_ready:
            asyncio.get_event_loop().run_until_complete((communicator.send_message("Python: while-true")))
