"""
format of json:
    sender_name = sender
    mood = mood
    mood_message = description in discord
    payload_json = {
        'content': sender_name + " sent you a message!",
        "tts": 0,
        "embeds":[
            {
            "title": "I'm feeling " + mood,
            "description": mood_message,
            "author": {
                "name": sender_name,
                "url": "https://discordapp.com" #update this for icons in message
                }
            }
        ]
    }
"""

class Message():
    def __init__(self,sender_name,mood, mood_message):
        self.sender_name = sender_name
        self.mood = mood
        self.mood_message = mood_message

    def create_json(self):
        self.payload_json = {
            'content': self.sender_name + " sent you a message!",
            "tts": 0,
            "embeds":[
                {
                "title": "Baby is feeling " + self.mood,
                "description": self.mood_message,
                "author": {
                    "name": self.sender_name,
                    "url": "https://discordapp.com"
                    }
                }
            ]
        }        
