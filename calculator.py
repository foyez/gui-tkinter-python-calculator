import tkinter

window = tkinter.Tk()
window.title('GUI')


# def say_hi():
#     tkinter.Label(window, text='Hi').pack()


# tkinter.Button(window, text='Click Me!', command=say_hi).pack()

def event_func(e):
    tkinter.Label(window, text='Event Executed').pack()


# <Button-1> for left click
# <Button-2> for middle click
# <Button-3> for right click
btn = tkinter.Button(window, text='Click Me!')
btn.bind('<Button-1>', event_func)
btn.pack()

window.mainloop()
