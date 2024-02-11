import tkinter as tk
from functions import info_response, init_alpha, weather_main
import sys
import threading

### This file is solely for the GUI ###

init_alpha()

# Handles text input by spawning a new thread to avoid halting the GUI
def handleText():
    # This function is just used here to help with multithreading
    def get_response(text_in):
        text_out = info_response(text_in)
        textField.delete(1.0, tk.END)
        textField.insert(tk.END, text_out)

    text = textField.get(1.0, "end-1c")
    textField.delete(1.0, tk.END)
    textField.insert(tk.END, "Loading...")
    
    temp_thread = threading.Thread(target=get_response, args=(text,), daemon=True)
    temp_thread.start()


# Gets and displays the weather
def weather_handler():
    try:
        weather['text'] = "Current temperature: " + weather_main()
    except Exception as e:
        print("Weather error:\n" + str(e))
        weather['text'] = "Weather is currently disconnected"


# Updates the screen periodically
# maybe make into multiple functions for different tasks
def update():
    weather_thread = threading.Thread(target=weather_handler, daemon=True)
    weather_thread.start()
    window.after(3_600_000, update) # waits 1 hour before updating again


# Initialize and run GUI things below
window = tk.Tk()
window.title("ISAAC")

weather = tk.Label(window, text="Please wait")
textField = tk.Text(window, height=5, width=45)
textField.insert(tk.END, "Talk to ISAAC here")
button = tk.Button(window, text = "Submit Text", command = handleText)

weather.pack()
textField.pack()
button.pack()

window.after(1, update)
window.mainloop()
sys.exit()