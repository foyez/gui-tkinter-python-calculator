import tkinter
import tkinter.messagebox


window = tkinter.Tk()
window.title('GUI')


def function():
    pass


# creating a root menu to insert all the sub menu
root_menu = tkinter.Menu(window)
window.config(menu=root_menu)

# creating a simple alert box
tkinter.messagebox.showinfo("Alert Message", "This is just a alert message!")

# creating a question to get the response from the user [Yes or No]
res = tkinter.messagebox.askquestion('Simple Question', 'Do you love Python?')
print(res)

if res == 'yes':
    tkinter.Label(window, text='You love Python!').pack()
else:
    tkinter.Label(window, text='You don\'t love Python!').pack()

window.mainloop()
