import requests
import json
import config

webhook_url = config.webhook_url

#bearer = holding the token
#number after = public client id
headers = {'Content-Type': 'application/json',
           'Authorization': '{}'.format('Bearer',config.auth_key)
}

def authentification():
    #can add diff urls in OAuth2 redirect tab in dashboard
    #current url is from discord's webhook channel
    response = requests.get(webhook_url, headers = headers)
    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return None


#does 0auth2, and then checks if there's an account --> if everything is good it will post to the url link
acc_info = authentification()
if acc_info is not None:
    try:
        requests.post(webhook_url, headers = headers, json = payload_json)
        print("Sending message to Discord Channel via Webhook")
    except:
        print("Error! Issue with authentification")
else:
    print('Request failed!')
