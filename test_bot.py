
import requests

def telegram_bot_sendtext(bot_message):
    
    bot_token = 'APIKEY'
    bot_chatID = [
        {"users" : "nazmudin", "id_bot" : "id"},
        {"users" : "raka", "id_bot" : "id"}
    ]
    
    for bot_id in bot_chatID:
        send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_id['id_bot'] + '&parse_mode=Markdown&text=' + bot_message
        response = requests.get(send_text)
    
    return response.json()

telegram_bot_sendtext("Test")
