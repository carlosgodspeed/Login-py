import tkinter as tk

def login():
    username = username_entry.get()
    password = password_entry.get()

    if username == "admin" and password == "password":
        login_status.config(text="Login successful!")
    else:
        login_status.config(text="Invalid login. Please try again.")

root = tk.Tk()
root.geometry("200x200")

username_label = tk.Label(root, text="Username:")
username_label.pack()

username_entry = tk.Entry(root)
username_entry.pack()

password_label = tk.Label(root, text="Password:")
password_label.pack()

password_entry = tk.Entry(root, show="*")
password_entry.pack()

login_button = tk.Button(root, text="Login", command=login)
login_button.pack()

login_status = tk.Label(root, text="")
login_status.pack()

root.mainloop()
