#author Kedir G. Gamada
#Date: 5/13/2023
#This gui program accepts temprature in degree centegrade and converts to degree F.


import tkinter as tk
window = tk.Tk()

window.title("Degree Centigrade to Ferhanite Convertor")


window.rowconfigure(0, minsize=200, weight=1)
window.columnconfigure(1, minsize=200, weight=1)


label_degre = tk.Label(window, text="Enter temprature in degree centigrade.", font=('Times New Roman', 15, 'bold'))
label_degre.grid(column=0, row=0, sticky="wne")
entry_degree = tk.Entry(window, width=35)
entry_degree.grid(column=0, row=1)
label_result = tk.Label(window, text="0" ,font=(28), fg="green")
label_result.grid(column=0, row=1)

def convert_to_f():
    degree_input = entry_degree.get()
    degree_input = float(degree_input)
    degree_farhaniate = degree_input*9/5+32
    label_result["text"] = f"The temprature is {degree_farhaniate} degree farhanite."

#Buttons to call function
degree_button = tk.Button(window, text="convert", command=convert_to_f, bg="green", fg="black").grid(column=0, row=4, padx=5, pady=5)
exit_button = tk.Button(window, text="Exit", command="exit", bg='gray', width=25).grid(column=1, row=4, padx=5, pady=5)

window.mainloop()
