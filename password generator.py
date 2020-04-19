
# generate a password with a length chosen and save it in a .txt file
import tkinter as tk
import random


root= tk.Tk()

canvas1 = tk.Canvas(root, width = 400, height = 400,  relief = 'raised')
canvas1.pack()

label1 = tk.Label(root, text='Password Generator',fg='dodger blue')
label1.config(font=('Calibri', 25))
canvas1.create_window(200, 25, window=label1)

label2 = tk.Label(root, text='Type your password length please: ')
label2.config(font=('Calibri', 16))
canvas1.create_window(200, 100, window=label2)

label3 = tk.Label(root, text='Type where will you use this password:')
label3.config(font=('Calibri', 16))
canvas1.create_window(200, 200, window=label3)

label7 = tk.Label(root, text='By Ahmed Hammami',fg='dodgerBlue2')
label7.config(font=('Calibri', 10))
canvas1.create_window(200, 50, window=label7)

entry1 = tk.Entry (root) 
canvas1.create_window(200, 150, window=entry1)

entry2 = tk.Entry (root) 
canvas1.create_window(200, 250, window=entry2)


def getpassword ():
    
    length = int(entry1.get())
    util =entry2.get()
    source = "01234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#&_- "
    password =  "".join(random.sample(source,length))
    text=util+': '+password
    f=open('your password.txt','w')
    f.write(text)
    f.close()
    
    label4 = tk.Label(root, text= 'your '+util+' password is:',font=('Calibri', 13))
    canvas1.create_window(200, 280, window=label4)
    
    label5 = tk.Label(root, text= password ,font=('Calibri', 13, 'bold'))
    canvas1.create_window(200, 305, window=label5)
    
    label6 = tk.Label(root, text= 'We have created a file password.txt' ,font=('Calibri', 12, 'bold'))
    canvas1.create_window(200,330 , window=label6)
    
button1 = tk.Button(text='Get the password ', command=getpassword, bg='brown', fg='white', font=('Calibri', 12, 'bold'))
canvas1.create_window(200, 360, window=button1)

root.mainloop()

