import requests

def LINE(message,access_token):
    url = "https://notify-api.line.me/api/notify"
    headers = {'Authorization': 'Bearer ' + access_token}
    payload = {'message': message}
    r = requests.post(url, headers=headers, params=payload,)
