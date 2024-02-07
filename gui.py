import tkinter as tk
from functions import info_response, init_alpha


init_alpha()
def handleText():
    text = textField.get(1.0, "end-1c")
    result = info_response(text)
    textField.delete(1.0, tk.END)
    textField.insert(tk.END, result)


window = tk.Tk()
window.title("ISAAC")

weather = tk.Label(window, text="Weather")
textField = tk.Text(window, height=5, width=45)
textField.insert(tk.END, "Talk to ISAAC here")
button = tk.Button(window, text = "Submit Text", command = handleText)

weather.pack()
textField.pack()
button.pack()

window.mainloop()