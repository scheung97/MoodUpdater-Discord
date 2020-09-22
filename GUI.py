import tkinter as tk
from tkinter import font, messagebox
import os
import message as msg
import authentification as auth
import requests

def greeting_msg(): #future idea: implement a way of verifying the message was sucessful
    """
    Creates pop-up window stating that the message was sent
    :Param: None
    :Return: None
    """
    messagebox.showinfo("Message Window", "Message sent! Tell them to check their Discord!")

def error_msg(Message):
    """
    Creates pop-up window stating error occurred
    :Param: None
    :Return: None
    """
    messagebox.showerror("Error!", Message)

def send_json(val):
    """
    Creates payload_json and sends via POST request with Discord API
    :Param: mood specified by the user
    :return: None
    """
    acc_info = auth.authentification()
    try:
        if val == 1:
            disc_msg = msg.Message("name", "sad", "i'm baby")
        elif val == 2:
            disc_msg = msg.Message("name", "sad", "i'm baby")
        elif val == 3:
            disc_msg = msg.Message("name", "sad", "i'm baby")
        elif val == 4:
            disc_msg = msg.Message("name", "sad", "i'm baby")
        elif val == 5:
            disc_msg = msg.Message("name", "sad", "i'm baby")
        elif val == 6:
            disc_msg = msg.Message("name", "sad", "i'm baby")
        try:
            disc_msg.create_json()

            #checks if there's any account information, and if so, tries to send the post request
            if acc_info is not None:
                try:
                    requests.post(auth.webhook_url, headers = auth.headers, json = disc_msg.payload_json)
                    greeting_msg()
                    print("Sending message to Discord Channel via Webhook")
                except:
                    error_msg("Error! Issue with authentification")
                    print("Error! Issue with authentification")
                    pass
            else:
                error_msg("No API account information found")
                print('Request failed!')

        except:
            error_msg("Error when creating json!")
            pass
    except ValueError:
        error_msg("Not a valid mood!")
        pass



########################################################################################################################################################################################################################################################################################################################
# GUI class
########################################################################################################################################################################################################################################################################################################################
class GUI():
    def __init__(self,master):
        self.height,self.width = 700, 550
        self.dir_path =  os.path.dirname(os.path.realpath(__file__))


        #main_window
        self.main_window = tk.Canvas(master, height = self.height, width = self.width)
        self.main_window.grid(row = 0, column = 0, sticky = "n,s,e,w")

        #title w/ text "Mood Ping"
        self.titleFont = font.Font(family = "Verdana", size = 22, weight = "bold", slant = "italic", underline = 0) #would have liked more font optons
        self.title = tk.Label(self.main_window, text = "Mood Ping!", font = self.titleFont)
        self.title.grid(row = 0, columnspan = self.width    , sticky = "n,e,s,w")

        #window for all the UI stuff
        self.ui_window = tk.Frame(self.main_window, bg = "#ffffff", width = self.width,  height = (self.height - 20))
        self.ui_window.grid(rowspan = self.height - 20, columnspan = self.width)

        #emotion widgets [implementing as buttons rn, will add more details later!]
        #func ran once and didn't update on button push, doing research I found out that a lambda is needed for the "command" to get the current state


        self.devmode = 0 #if 1, will disable all buttons except one; if 0, buttons will all be functional
        if self.devmode == 1:
            self.button_state = "disabled"
        else:
            self.button_state = "active"

        #TODO: update lambda function to call message creation w/ variable messages

        self.sadButton = tk.Button(self.ui_window, text = "I'm baby", state = "active", command = lambda: send_json(1))
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

########################################################################################################################################################################################################################################################################################################################
# Runs the program
########################################################################################################################################################################################################################################################################################################################
if __name__ == "__main__":
    root = tk.Tk() #makes the window
    root.title("DiscordMoodPing")
    DiscordMoodPing = GUI(root)
    root.mainloop() #necessary to run
