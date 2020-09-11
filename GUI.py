import tkinter as tk
import os

########################################################################################################################################################################################################################################################################################################################
# GUI class
########################################################################################################################################################################################################################################################################################################################
class GUI():
    def __init__(self,master):
        self.height,self.width = 700, 550
        self.dir_path =  os.path.dirname(os.path.realpath(__file__))

        #main_window
        main_window = tk.Canvas(master, bg = "red", height = self.height, width = self.width)
        main_window.pack()
        #main_window.pack(fill = "both", expand = "true") #do i want the canvas to change as the window does??? probably not..

        #window for all the UI stuff
        ui_window = tk.Frame(main_window, bg = "blue", width = self.width,  height = (self.height - 20))
        ui_window.place(relx = 0.003, rely = 0.075) #is there an easier way to get this fitting w/out the tinkering?

        #title at top = label for the rest of the widgets??
        title = tk.Label(main_window, text = "Mood Ping!")
        #title.place(side = "top", fill = "x")










        
    #methods for retrieving info can be here

########################################################################################################################################################################################################################################################################################################################
# Runs the program
########################################################################################################################################################################################################################################################################################################################
if __name__ == "__main__":
    root = tk.Tk() #makes the window
    root.title("DiscordMoodPing")
    needySO_app = GUI(root)
    root.mainloop() #necessary to run
