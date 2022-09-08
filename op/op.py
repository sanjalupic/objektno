import tkinter as tk
import threading as thr
import socket


root = tk.Tk()
canvas = tk.Canvas(root, bg="#C0C0C0", width=400, height=700)
canvas.pack()


def add(num1, num2):
    canvas.delete("all")
    x = int(num1)
    y = int(num2)
    r = x + y
    text = "The result of addition " + \
        str(x) + " and " + str(y) + " is: " + str(r)
    canvas.create_text(120, 100, text=text,
                       fill="black", font=('Times 12'))


def subtract(num1, num2):
    canvas.delete("all")
    x = int(num1)
    y = int(num2)
    r = x - y
    text = "The result of sharing " + \
        str(x) + " and " + str(y) + " is " + str(r)
    canvas.create_text(120, 100, text=text,
                       fill="black", font=('Times 12'))


def multiply(num1, num2):
    canvas.delete("all")
    x = int(num1)
    y = int(num2)
    r = x * y
    text = "The result of multiplication " + \
        str(x) + " and " + str(y) + " is: " + str(r)
    canvas.create_text(120, 100, text=text,
                       fill="black", font=('Times 12'))


def divide(num1, num2):
    canvas.delete("all")
    x = int(num1)
    y = int(num2)
    r = x / y
    text = "The result of sharing " + \
        str(x) + " and " + str(y) + " is: " + str(r)
    canvas.create_text(120, 100, text=text,
                       fill="black", font=('Times 12'))


def Srv_func(cs):
    while True:
        message = cs.recv(1024).decode()
        print(message)
        x = message.split()
        if x[0] == "Add":
            equal = add(x[1], x[2])
        elif x[0] == "Subtract":
            equal = subtract(x[1], x[2])
        elif x[0] == "Multiply":
            equal = multiply(x[1], x[2])
        elif x[0] == "Divide":
            equal = divide(x[1], x[2])


def str_func():
    listensocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port = 8000
    maxConnections = 10
    name = socket.gethostname()
    listensocket.bind(("localhost", port))
    listensocket.listen(maxConnections)
    serverMessage = "Started server at " + name + " on port " + str(port)
    print(serverMessage)
    canvas.create_text(200, 650, text=serverMessage,
                       fill="black", font=('Times 10'))
    canvas.pack()
    while True:
        (clientsocket, address) = listensocket.accept()
        print("New connection made from address: ", address)
        t = thr.Thread(target=Srv_func, args=(clientsocket,))
        t.daemon = True
        t.start()


def startServer():
    t1 = thr.Thread(target=str_func)
    t1.daemon = True
    t1.start()


menu = tk.Menu(root)
root.config(menu=menu)
serverMenu = tk.Menu(menu, tearoff=False)
serverMenu.add_command(command=startServer, label="Start Server")
menu.add_cascade(label="Server", menu=serverMenu)


root.mainloop()
