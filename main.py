import tkinter
from tkinter import messagebox
# import library

window = tkinter.Tk()
window.title('Login from')
window.geometry('400x500')
window.configure(bg='#696969')

# login function
def login():
    username = "login"
    password = "admin123"
    if username_entry.get()==username and password_entry.get()==password:
        messagebox.showinfo(title='Login success',
                            message='Login successfully completed')
    else:
        messagebox.showerror(title='Error', message='Invalid password')


frame = tkinter.Frame(bg='#696969')


# Create widgets
login_label = tkinter.Label(
    frame, text='Login', bg='#696969', fg='#FFFF00', font=('SimSun', 30))
username_label = tkinter.Label(
    frame, text='Username', bg='#696969', fg='#FFFFFF', font=('SimSun', 16))
password_label = tkinter.Label(
    frame, text='Password', bg='#696969', fg='#FFFFFF', font=('SimSun', 16))
username_entry = tkinter.Entry(frame, font=('SimSun', 16))
password_entry = tkinter.Entry(frame, show='*', font=('SimSun', 16))
login_button = tkinter.Button(
    frame, text='Login', bg='#FFFF00', fg='#000000', font=('SimSun', 16), command=login)

# widget placement on the screen
login_label.grid(row=0, column=0, columnspan=2, sticky='news', pady=40)
username_label.grid(row=1, column=0)
username_entry.grid(row=1, column=1, pady=20)
password_label.grid(row=2, column=0)
password_entry.grid(row=2, column=1, pady=20)
login_button.grid(row=3, column=0, columnspan=2, pady=30)


frame.pack()

window.mainloop()
