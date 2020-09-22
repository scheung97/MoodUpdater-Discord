import requests
import json
import config

webhook_url = config.webhook_url

#bearer = holding the token
#number after = public client id
headers = {'Content-Type': 'application/json',
           'Authorization': 'Bearer ' + config.auth_key
}
def authentification():
    #can add diff urls in OAuth2 redirect tab in dashboard
    #current url is from discord's webhook channel
    response = requests.get(webhook_url, headers = headers)
    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return None
