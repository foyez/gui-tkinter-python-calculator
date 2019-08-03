import tkinter


class GuiPractice:
    def __init__(self, window):
        self.text_btn = tkinter.Button(
            window, text='Click Me!', command=self.say_hi)
        self.text_btn.pack()

        self.close_btn = tkinter.Button(
            window, text='Close', command=window.quit)
        self.close_btn.pack()

    def say_hi(self):
        tkinter.Label(window, text='Hi').pack()


window = tkinter.Tk()
window.title('GUI')

gui_practice = GuiPractice(window)

window.mainloop()
