so_name = "Spenser"
mood = "Sad"
Sad_mood = "I'm baby"
payload_json = {
    'content': so_name + " sent you a message!",
    "tts": 0,
    "embeds":[     #type in the docs here (doc says "embed" not "embeds")
        {
        "title": "Baby is feeling " + mood,
        "description": Sad_mood,
        "author": {
            "name": so_name,
            "url": "https://discordapp.com" #heart emoji here
            }
        }
        #struggle with the embed b/c [] weren't in the docs, and there was a typo in the docs
    ]
}

webhook_url = "https://discordapp.com/api/webhooks/{ClientId}/asdfasdfasdfadfasasdfasdfasdfasdfasdfasdf"

class Message():
    def __init__(self,so_name,mood, mood_msg):
        self.so_name = so_name
        self.mood = mood
        self.mood_msg =
        pass
    pass
