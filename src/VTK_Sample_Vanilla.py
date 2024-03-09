import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=170
        height=50
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GButton_865=tk.Button(root)
        GButton_865["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Times',size=10)
        GButton_865["font"] = ft
        GButton_865["fg"] = "#000000"
        GButton_865["justify"] = "center"
        GButton_865["text"] = "Hello"
        GButton_865.place(x=10,y=10,width=70,height=25)
        GButton_865["command"] = self.GButton_865_command

        GLabel_52=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_52["font"] = ft
        GLabel_52["fg"] = "#333333"
        GLabel_52["justify"] = "center"
        GLabel_52["text"] = "World"
        GLabel_52.place(x=90,y=10,width=70,height=25)

    def GButton_865_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
