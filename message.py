import os

class Message():
    """ Basic formatted JSON required for calling the Discord API

    Attributes:
        sender_name         Name of the person using the app (hardcoded for now)
        mood                How the user is feeling emotionally
        mood_message        Preset message associated with each mood
    """

    def __init__(self, mood, mood_message):
        self.sender_name = sender_name
        self.mood = mood
        self.mood_message = mood_message

    def create_json(self):
        self.payload_json = {
            "username": "DiscordMoodPing", #overrides old username b/c i wanted to change the name
            "avatar_url" : "https://www.freepnglogos.com/uploads/heart-png/emoji-heart-33.png", #how do i keep this on the machine
            "content": self.sender_name + " sent you a message!",
            "tts": 0,
            "embeds":[
                {
                "title": "I'm feeling " + self.mood,
                "description": self.mood_message #,
                #"author": {
                #    "name": self.sender_name,
                #    "url": "https://discordapp.com/" #update this for icons in discord message
                #    }
                }
            ]
        }
