import threading
from time import sleep
import functions
from multiprocessing import Process
import asyncio
import os


if __name__ == '__main__':
    os.system("bash gui_runner.sh")
    ### Various threads ###
    functions.init_alpha()
    weather_thread = threading.Thread(target=functions.weather_main, daemon=True)
    weather_thread.start()
    
    ### End of other threads ###

    ### Main thread / program ###
    # This thread should last the longest (possibly while-true loop)


    while (True):
        
        temperature = asyncio.get_event_loop().run_until_complete(functions.get_weather())
        print(temperature)
        sleep(1800) # 30 minutes

    ### End of main thread ###




### Simple templates of various functionalities ###
    ## How to send a message to java:
        # asyncio.get_event_loop().run_until_complete((communicator.send_message("A message")))

### End of templates ###


### Beginning of codes to/from Java ###
"""
    Messages should be sent in the form of number:message (no spaces between number and message)
    Ex) 0000:Debug information

    0001 - 0099 : Information from Python to Java
    0100 - 9900 : Information from Java to Python
    0000 : Can be used either way

    * 0000 : Sends debug information (shoud be printed to console)

    * 0001 : Sends any information (not displayed)
    * 0002 : Sends information to display (ISAAC response box)
    * 0003 : Sends weather information
    * 0004 : 

    * 0100 : Sends any information (not displayed)
    * 0200 : Sends information from ISAAC input field
    * 0300 : 
"""
### End of codes to/from Java ###