import threading
from time import sleep
import functions
import os
import sys


if __name__ == '__main__':
    gui_thread = threading.Thread(target=os.system, args=("python3 gui.py",))
    gui_thread.start()
    print("Moving on...")


    ### Main thread / program ###
    # This thread should last the longest (possibly while-true loop)

    # Ends when GUI closes
    gui_thread.join()

    ### End of main thread ###