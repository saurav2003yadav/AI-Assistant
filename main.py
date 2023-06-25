import speech_recognition as sr
import os
import webbrowser
import openai
from config import apikey
import datetime
import random

# todo 1: this help to make direct interaction to the JARVIS
chatstr = ""
def chat(query):
    global chatstr
    print(chatstr)
    openai.api_key = apikey
    chatstr += f"Saurav: {query}\n JARVIS: "
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt= chatstr,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # todo: wrap this inside a tru catch block
    say(response["choices"][0]["text"])
    chatstr += f"{response['choices'][0]['text']}\n"
    return response["choices"][0]["text"]

    # with open(f"Openai/prompt- {random.randint(1, 2343434356)}", "w") as f:
    with open(f"Openai/{''.join(prompt.split('intelligence')[1:]).strip()}.txt", "w") as f:
        f.write(text)

# todo 2 : this help to make direct interaction to the JARVIS until here.between todo 1 and 2

# create function

def ai(prompt):
    openai.api_key = apikey
    text = f"Openai response for prompt:{prompt} \n **************************\n\n"

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # todo: wrap this inside a tru catch block
    print(response["choices"][0]["text"])
    text+=response["choices"][0]["text"]
    if not os.path.exists("Openai"):
        os.mkdir("Openai")

    # with open(f"Openai/prompt- {random.randint(1, 2343434356)}", "w") as f:
    with open(f"Openai/{''.join(prompt.split('intelligence')[1:]).strip() }.txt", "w") as f:
        f.write(text)
def say(text):
    os.system(f'say "{text}"')

# taking input of our speach or voice(mice command)
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.6
        audio = r.listen(source)
        try:
            print("Recognizing")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some Error Occured. Sorry from Jarvis"

if __name__ == '__main__':
    print('PyCharm')
    say("Hello I am  Jarvis A.I")
    while True:
        print("listening...")
        query = takeCommand()
        # todo : add more sites
        sites = [["youtube","https://www.youtube.com"],["google","https://www.google.com"],
                ["wikipedia","https://www.wikepedia.com"]]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} sir...")
                webbrowser.open(site[1])
        # todo : add a feature to play a specific song
        if "open music" in query:
            musicPath = "/Applications/Resso.app "
            os.system(f"open {musicPath}")
        # todo: if an error occure in this code then remove el from all elif starting from there
        elif "the time" in query:
            #strfTime = datetime.datetime.now().strftime("%H:%M:%S")
            #say(f"sir the time is {strfTime}")
            hour = datetime.datetime.now().strftime("%H")
            min = datetime.datetime.now().strftime("%M")
            say(f"sir the time is {hour} baajka {min} minutes")

        elif "open facetime".lower() in query.lower():
            os.system(f"open /System/Applications/FaceTime.app")


        elif "open Telegram".lower() in query.lower():
            os.system(f"open /Applications/Telegram.app ")

        elif "using artificial intelligence".lower() in query.lower():
            ai(prompt=query)

        elif "Jarvis quit".lower() in query.lower():
            exit()

        elif" reset chat".lower() in query.lower():
            chatstr = " "
        else:
            print("chatting.....")
            chat(query)




        #say(query)

