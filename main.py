import tkinter
# import library tkinter

window = tkinter.Tk()
window.title('Login from')
window.geometry('400x500')
window.configure(bg='#696969')

# Create widgets
login_label = tkinter.Label(
    window, text='Login', bg='#696969', fg='#FFFFFF', font=('SimSun', 28))
username_label = tkinter.Label(
    window, text='Username', bg='#696969', fg='#FFFFFF', font=('SimSun', 16))
username_entry = tkinter.Entry(window, font=('SimSun', 16))
password_label = tkinter.Label(
    window, text='Password', bg='#696969', fg='#FFFFFF', font=('SimSun', 16))
password_entry = tkinter.Entry(window, show='*', font=('SimSun', 16))
login_button = tkinter.Button(
    window, text='Login', bg='#2F4F4F', fg='#FFFFFF', font=('SimSun', 16))

# widget placement on the screen
login_label.grid(row=0, column=0, columnspan=2, sticky='news')
username_label.grid(row=1, column=0)
username_entry.grid(row=1, column=1)
password_label.grid(row=2, column=0)
password_entry.grid(row=2, column=1)
login_button.grid(row=3, column=0, columnspan=2)
window.mainloop()
