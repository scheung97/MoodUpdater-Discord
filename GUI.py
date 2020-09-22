import tkinter as tk
from tkinter import font, messagebox
import os, requests
import message as msg
import authentification as auth


def greeting_msg():
    """
    Creates pop-up window stating that the message was sent
    :Param: None
    :Return: None
    """
    messagebox.showinfo("Message Window", "Message sent! Tell them to check their Discord!")

def error_msg(Message):
    """Creates pop-up window stating error occurred

    :param: None
    :return: None
    """
    messagebox.showerror("Error!", Message)

def send_json(mood):
    """Creates payload_json and sends via POST request with Discord API

    :param mood: mood specified by the button the user clicks
    :raises ValueError: mood inputted doesn't correspond to any specified mood
    :return: None
    """
    acc_info = auth.authentification()
    try:
        if mood == "sad":
            disc_msg = msg.Message("Agnes", "sad", "I'm baby. I miss you :(")
        elif mood == "happy":
            disc_msg = msg.Message("Agnes", "happy", "I'm feeling great!")
        elif mood == "angry":
            disc_msg = msg.Message("Agnes", "angry", "I'm in a bad mood")
        elif mood == "needy":
            disc_msg = msg.Message("Agnes", "needy", "I'd like your love and attention please")
        elif mood == "love":
            disc_msg = msg.Message("Agnes", "in love", "I love you")
        elif mood == "unwell":
            disc_msg = msg.Message("Agnes", "bad", "I'm not feeling well")
        elif mood == "afraid":
            disc_msg = msg.Message("Agnes", "afraid", "I'm scared......")
        elif mood == "nervous":
            disc_msg = msg.Message("Agnes", "nervous", "I don't feel confident right now")
        elif mood == "communicate":
            disc_msg = msg.Message("Agnes", "ready", "We need to talk.")
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
        #self.dir_path = os.path.dirname(os.path.realpath(__file__))


        #main_window
        self.main_window = tk.Canvas(master, bg = "blue", height = self.height, width = self.width)
        self.main_window.grid(row = 0, column = 1, sticky = "n,s,e,w")

        #title w/ text "Mood Ping"
        self.titleFont = font.Font(family = "Verdana", size = 22, weight = "bold", slant = "italic", underline = 0) #would have liked more font optons
        self.title = tk.Label(self.main_window, bg = "blue", text = "Mood Ping!", font = self.titleFont)
        self.title.grid(row = 0, columnspan = self.width, sticky = "n,e,s,w")


        #user's name input
        self.inputs = tk.Frame(self.main_window, bg = "blue", width = self.width)
        self.inputs.grid(row = 1, columnspan = self.width, sticky = "n,e,s,w")

        blank = tk.Label(self.inputs, bg = "blue", text = "                          ") #helps with spacing cause grid() justifies to left automatically
        blank.grid(row = 0, column = 0 )
        self.name_label_font = font.Font(family = "Verdana", size = 11)
        self.name_label = tk.Label(self.inputs, bg = "blue", text = "Your Name: ", font = self.name_label_font)
        self.name_label.grid(row = 0, column =1)
        self.name_input = tk.Entry(self.inputs, font = self.name_label_font, width = 20)
        self.name_input.grid(row = 0, column = 2, padx = 8, pady = 9, sticky = "n,e,w,s")

        #button to get user's name

        """
        TODO: use get button as input for name 
        """
        self.name_button_font = font.Font(family = "Verdana", size = 9)
        self.name_button = tk.Button(self.inputs, text = "Set Name", font = self.name_button_font, padx = 1, pady = 1, command = lambda: set_name(self.name_input.get()))
        self.name_button.grid(row = 0, column = 3)

        #window for all the UI stuff
        self.ui_window = tk.Frame(self.main_window, bg = "blue", width = self.width,  height = (self.height - 20))
        self.ui_window.grid(rowspan = self.height - 20, columnspan = self.width)

        self.devmode = 0 #if 1, will disable all buttons except one; if 0, buttons will all be functional
        if self.devmode == 1:
            self.button_state = "disabled"
        else:
            self.button_state = "active"

        #emotion widgets [implementing as buttons rn, will add more details later!]
        #func ran once and didn't update on button push, doing research I found out that a lambda is needed for the "command" to get the current state

        #top row of buttons
        self.sadButton = tk.Button(self.ui_window, text = "I'm baby", state = "active", command = lambda: send_json("sad"))
        self.sadButton.place(x = 0, y = 0)
        self.happyButton = tk.Button(self.ui_window,text = "I'm so happy", state = self.button_state, command = lambda: send_json("happy"))
        self.happyButton.place(x = 230  , y = 0)
        self.madButton = tk.Button(self.ui_window, text = "I'm angy", state = self.button_state, command = lambda: send_json("angry"))
        self.madButton.place(x = 493, y = 0)

        #middle row of buttons
        self.needyButton = tk.Button(self.ui_window, text = "I'm feeling needy", state = self.button_state, command = lambda: send_json("love"))
        self.needyButton.place(x = 0, y = 300)
        self.loveButton = tk.Button(self.ui_window, text = "I love you", state = self.button_state, command = lambda: send_json("needy"))
        self.loveButton.place(x = 240, y = 300)
        self.sickButton = tk.Button(self.ui_window, text = "I don't feel so well", state = self.button_state, command = lambda: send_json("unwell"))
        self.sickButton.place(x = 444, y = 300)

        #bottom row of buttons
        self.afraidButton = tk.Button(self.ui_window, text = "I'm scared", state = self.button_state, command = lambda: send_json("afraid"))
        self.afraidButton.place(x = 0, y = 654)
        self.nervousButton = tk.Button(self.ui_window, text = "I'm nervous", state = self.button_state, command = lambda: send_json("nervous"))
        self.nervousButton.place(x = 239, y = 654)
        self.communicationButton = tk.Button(self.ui_window, text = "I want to talk", state = self.button_state, command = lambda: send_json("communicate"))
        self.communicationButton.place(x = 471, y = 654)
        """
        if badnewsButton == 1:
            print("good luck buddy")
        set status == "fucked"
        """
########################################################################################################################################################################################################################################################################################################################
# Runs the program
########################################################################################################################################################################################################################################################################################################################
if __name__ == "__main__":
    root = tk.Tk() #makes the window
    root.title("DiscordMoodPing")
    DiscordMoodPing = GUI(root)
    root.mainloop() #necessary to run
