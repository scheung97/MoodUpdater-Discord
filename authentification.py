import requests
import json

# redirect URI from OAuth2 section of Discord's developer portal:
# https://discord.com/developers/applications/{ClientId}/oauth2"
webhook_url = "https://discordapp.com/api/webhooks/{ClientId}/{more}"


headers = {'Content-Type': 'application/json',
           'Authorization': 'Bearer {ClientId}'
}

def authentification():
    response = requests.get(webhook_url, headers = headers)
    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return None

acc_info = authentification()
if acc_info is not None:
    try:
        requests.post(webhook_url, headers = headers, json = payload_json)
        print("Sending message to Discord Channel via Webhook")
    except:
        print("Error! Issue with authentification")
else:
    print('Request failed!')
