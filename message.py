"""
format:
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
                "description": self.mood,
                "author": {
                    "name": self.sender_name,
                    "url": "https://discordapp.com"
                    }
                }
            ]
        }


    """
    do i need??

    def set_sendername(self, sender_name):
        self.sender_name = sender_name

    def get_sendername(self):
        return self.sender_name

    def set_mood(self, mood):
        self.mood = mood

    def get_mood(self):
        return self.mood
    """




"""
#create msg obj with sender and mood
msg = Message("Kevin", "sad")

#creates payload_json based on obj variables
msg.get_json()
print(msg.payload_json)

#setters to update obj variables
msg.set_sendername("Albert")
msg.set_mood("angry")
"""
