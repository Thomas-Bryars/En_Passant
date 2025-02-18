import tkinter as tk

def close_after_delay():
    root.destroy()

root = tk.Tk()
root.title("Tkinter Example")
label = tk.Label(root, text="Hello, Tkinter!")
label.pack()

# Close the window after 10 seconds (10000 milliseconds)
root.after(10000, close_after_delay)

root.mainloop()