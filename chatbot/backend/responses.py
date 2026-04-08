import random
import requests

previous_message = ""

def bot_response(message):
    global previous_message

    if message == "hello":
        response = "OK hello"

    elif message == "goodbye":
        response = "don't want to meet you"

    elif message == "Gimme image":
        random_number = random.randint(10000, 100000)
        image_url = f"https://picsum.photos/400/300?id={random_number}"
        response_text = f'<img src="{image_url}">'
        response = response_text

    elif message.startswith("Tell me about"):
        word = message[13:]

        url = f"https://en.wikipedia.org/wiki/{word}"

        response_text = f'<a href="{url}">Wikipedia article about {word}</a>'

        response = response_text

    elif previous_message == message:
        response = "STOP REPEATING YOURSELF!!!"

    elif message.startswith("Weather in"):
        city = message[11:]
        API_key = "c916e1ae29ac4c66b9a71153260604"

        url = f"http://api.weatherapi.com/v1/current.json?key={API_key}&q={city}"
        try:
            response = requests.get(url)
            data = response.json()
            
            temp = data['current']['temp_c']
            
            response = f"Weather in {city} is currently {temp}°C."

        except:
            response = "I couldn't find the weather for that location."

    elif message == "help":
        help_text = "<b>Here are the commands I know:</b>"
        help_text += "<ul>"
        help_text += "<li><b>hello</b> - GET OK Hello</li>"
        help_text += "<li><b>goodbye</b> - GET don't want to meet you again</li>"
        help_text += "<li><b>Gimme image</b> - See a random photo</li>"
        help_text += "<li><b>Tell me about [something]</b> - GET a Wikipedia link</li>"
        help_text += "<li><b>Weather in [location]</b> - GET weather</li>"
        help_text += "<li><b>help</b> - Show this list</li>"
        help_text += "</ul>"
    
        response = help_text

    else:
        response = "stupid!!!"

    previous_message = message

    return response 