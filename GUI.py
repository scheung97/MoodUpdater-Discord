import tkinter as tk
from tkinter import font
import os

########################################################################################################################################################################################################################################################################################################################
# GUI class
########################################################################################################################################################################################################################################################################################################################
def test_func(val):
    if val == 1:
        print("I'm baby")
    elif val == 2:
        print("I'm so happy")
    elif val == 3:
        print("I'm angy >:((")
    elif val == 4:
        print("I love you <3")
    else:
        print("Mood not found, please enter a valid input")

class GUI():
    def __init__(self,master):
        self.height,self.width = 700, 550
        self.dir_path =  os.path.dirname(os.path.realpath(__file__))
        self.devmode = 0 #if 1, will disable all buttons except one; if 0, buttons will all be functional




        #main_window
        self.main_window = tk.Canvas(master, bg = "red", height = self.height, width = self.width)
        self.main_window.pack()
        #main_window.pack(fill = "both", expand = "true") #do i want the canvas to change as the window does??? probably not..

        #window for all the UI stuff
        self.ui_window = tk.Frame(self.main_window, bg = "blue", width = self.width,  height = (self.height - 20))
        self.ui_window.place(relx = 0.003, rely = 0.075) #is there an easier way to get this fitting w/out the tinkering?

        #title at top = label for the rest of the widgets??
        self.titleFont = font.Font(family = "Verdana", size = 22, weight = "bold", slant = "italic", underline = 0) #would have liked more font optons
        self.title = tk.Label(self.main_window, bg = "yellow", text = "Mood Ping!", font = self.titleFont)
        self.title.place( height = 52.5, relwidth = 1) #not sure how to get the perfect measurements without hard coding in these values

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
        self.sadButton = tk.Button(self.ui_window, text = "I'm baby", command = lambda: test_func(1))
        self.sadButton.place(relx = 0, rely = 0)
        self.happyButton = tk.Button(self.ui_window,text = "I'm so happy", state = self.button_state, command = lambda: test_func(2))
        self.happyButton.place(relx = 0.1, rely = 0.1)
        self.madButton = tk.Button(self.ui_window, text = "I'm angy", state = self.button_state, command = lambda: test_func(3))
        self.madButton.place(relx = 0.2, rely = 0.2)
        self.loveButton = tk.Button(self.ui_window, text = "I love you", state = self.button_state, command = lambda: test_func(4))
        self.loveButton.place(relx = 0.3, rely = 0.3)







    #methods for retrieving info can be here

########################################################################################################################################################################################################################################################################################################################
# Runs the program
########################################################################################################################################################################################################################################################################################################################
if __name__ == "__main__":
    root = tk.Tk() #makes the window
    root.title("DiscordMoodPing")
    needySO_app = GUI(root)
    root.mainloop() #necessary to run
