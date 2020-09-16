import tkinter as tk
from tkinter import font
import os

########################################################################################################################################################################################################################################################################################################################
# GUI class
########################################################################################################################################################################################################################################################################################################################


class GUI():
    def __init__(self,master):
        self.height,self.width = 700, 550
        self.dir_path =  os.path.dirname(os.path.realpath(__file__))
        self.devmode = 0 #if 1, will disable all buttons except one; if 0, buttons will all be functional


        #main_window
        self.main_window = tk.Canvas(master, bg = "red", height = self.height, width = self.width)
        self.main_window.grid(row = 0, column = 0, sticky = "n,s,e,w")
        #self.main_window.pack()
        #main_window.pack(fill = "both", expand = "true") #do i want the canvas to change as the window does??? probably not..

        #title at top = label for the rest of the widgets??
        self.titleFont = font.Font(family = "Verdana", size = 22, weight = "bold", slant = "italic", underline = 0) #would have liked more font optons
        self.title = tk.Label(self.main_window, bg = "yellow", text = "Mood Ping!", font = self.titleFont)#.grid(row = 0, columnspan = self.width, sticky = "n,e,s,w")
        self.title.grid(row = 0, columnspan = self.width, sticky = "n,e,s,w")

        #window for all the UI stuff
        self.ui_window = tk.Frame(self.main_window, bg = "blue", width = self.width,  height = (self.height - 20))
        self.ui_window.grid(rowspan = self.height - 20, columnspan = self.width)

        #emotion widgets [implementing as buttons rn, will add more details later!]
        #func ran once and didn't update on button push, doing research I found out that a lambda is needed for the "command" to get the current state
        if self.devmode == 1:
            self.button_state = "disabled"
        else:
            self.button_state = "active"

        """
        To Do here:
            update lambda function to call message creation w/ variable messages
        """

        #replace place() w/ grid() for easier formatting
        self.sadButton = tk.Button(self.ui_window, text = "I'm baby", state = "active", command = lambda: test_func(1))
        self.sadButton.place(x = 0, y = 0)
        self.happyButton = tk.Button(self.ui_window,text = "I'm so happy", state = self.button_state, command = lambda: test_func(2))
        self.happyButton.place(x = 230  , y = 0)
        self.madButton = tk.Button(self.ui_window, text = "I'm angy", state = self.button_state, command = lambda: test_func(3))
        self.madButton.place(x = 493, y = 0)

        self.loveButton = tk.Button(self.ui_window, text = "I love you", state = self.button_state, command = lambda: test_func(4))
        self.loveButton.place(x = 240, y = 300)
        self.needyButton = tk.Button(self.ui_window, text = "I'm feeling needy", state = self.button_state, command = lambda: test_func(5))
        self.needyButton.place(x = 0, y = 300)
        self.sickButton = tk.Button(self.ui_window, text = "I don't feel so well", state = self.button_state, command = lambda: test_func(6))
        self.sickButton.place(x = 444, y = 300)

    #methods for retrieving info can be here
    def test_func(val):
        try:
            if val == 1:
                print("I'm baby")
            elif val == 2:
                print("I'm so happy")
            elif val == 3:
                print("I'm angy >:((")
            elif val == 4:
                print("I love you <3")
            elif val == 5:
                print("I'm needy")
            elif val == 6:
                print("I don't feel so good mr. stark")
        except ValueError:
            pass
########################################################################################################################################################################################################################################################################################################################
# Runs the program
########################################################################################################################################################################################################################################################################################################################
if __name__ == "__main__":
    root = tk.Tk() #makes the window
    root.title("DiscordMoodPing")
    needySO_app = GUI(root)
    root.mainloop() #necessary to run
