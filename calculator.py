import tkinter
import tkinter.messagebox


window = tkinter.Tk()
window.title('GUI')


def function():
    pass


# creating a root menu to insert all the sub menu
root_menu = tkinter.Menu(window)
window.config(menu=root_menu)

# creating the 'Canvas' area of width and height 500px
canvas = tkinter.Canvas(window, width=500, height=200)
canvas.pack()

# taking image from the directory and storing the source in a variable
icon = tkinter.PhotoImage(file='img/linux.png')
# displaying the picture using a 'Label' by passing the 'picture' variable to 'image' parameter
label = tkinter.Label(window, image=icon)
label.pack()

window.mainloop()
