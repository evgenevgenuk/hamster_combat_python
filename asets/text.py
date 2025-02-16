import tkinter as tk
root = tk.Tk()
root.title("tk program")
root.geometry("400x400")
root.resizable(False, False)
label = tk.Label(root, text="test tekst", font=("Arial", 30 , "bold",), bg="blue")
label.pack()
root.mainloop()
