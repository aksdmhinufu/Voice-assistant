# imports:
from __future__ import print_function
import pywhatkit as kit  # pip install pywhatkit
import speech_recognition as sr  # pip install SpeechRecognition
import pyttsx3  # pip install pyttsx3
import wikipedia  # pip install wikipedia
import pyjokes  # pip install pyjokes
import yagmail  # pip install yagmail
import wolframalpha  # pip install wolframalpha
from datetime import datetime  # built into python
import imaplib  # built into python
import traceback  # built into python
import email  # pip install
from cal_setup import get_calendar_service
from newspaper import fulltext
import newspaper
from functools import lru_cache
import requests
from bs4 import BeautifulSoup
from googlesearch import search
import threading
import time as t




print("initialising QUANDALE DINGLE'S GOOFY AHH MECHANICS")
global my_timer
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150)
FROM_EMAIL = "thestockdude10@gmail.com"
FROM_PWD = "pqnoalssfcodnous"
SMTP_SERVER = "imap.gmail.com"
def near_me(query):
    page = requests.get("https://www.google.com/maps/search/" + query)
    soup = BeautifulSoup(page.content, 'html.parser')
    place = soup.find(class_ = "hfpxzc")
    speak("Theres a " + place + " near you. Baised on its reviews, its " + gob + "")


def countdown(query):
    global my_timer
    URL = "https://www.google.co.in/search?q=" + query
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
    }
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    time4timer = soup.find(jsname="VQs5Rb").text.replace("h", " Hour ").replace("m", " minute ").replace("s", " seconds ").split()
    time4timer.pop(5)
    time4timer.pop(4)
    if "00" in time4timer[0]:
        time4timer.pop(0)
        time4timer.pop(0)
        if "00" in time4timer[0]:
            time4timer.pop(0)
            time4timer.pop(0)
    queryy = str(time4timer).replace("[", "").replace("'", "").replace(",", "").replace("]", "")
    #print(queryy)
    URL = "https://www.google.co.in/search?q=" + "Convert " + queryy + " to seconds"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
    }
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    time = soup.find(id="NotFQb")
    #print(time)
    timer = str(time)
    #print(timer)
    timey = timer.split(" ")
    time4timer = int(timey[9].replace('"', "").replace("/", "").replace(">", "").replace("value=", ""))
    my_timer = time4timer
    #print(time4timer)
    #countdown_thread = threading.Thread(target=countdown, args=(query))
    #countdown_thread.start()
    while time4timer > 1:
        time4timer -= 1
        t.sleep(1)
    speak("beep, beep, your timer has rung")
@lru_cache(100)
def recipie(query):
    URL = "site:spendwithpennies.com " + query
    for i in search(URL, tld="com", num=1):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
            }
        page = requests.get(str(i), headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        ingredients = soup.find("div", class_="wprm-recipe-ingredient-group").text
        speak_ingredients = ingredients.split("▢")
        recipie = soup.find("div", class_="wprm-recipe-instruction-group").text
        speak_recipie = recipie.split(".")
        print(ingredients)
        print(recipie)
        i = 0
        while i < len(speak_ingredients):
            i = i + 1
            speak("Here is the ingredents you will need. If you want when, just ask!")
            Next = take_command()
            while not "Bob" in Next:
                Next = take_command()
            speak(speak_ingredients[i])
        i = 0
        while i < len(speak_recipie):
            i = i + 1
            speak("Here is the recipe. Once you've completed a step, ask me and I'l go to the next one")
            Next = take_command()
            while not "Bob" in Next:
                Next = take_command()
            speak(speak_ingredients[i])
        speak("congrat's, you've made it!")
@lru_cache(100)
def stock_price(query):
   try:
        user_query = query

        URL = "https://www.google.co.in/search?q=" + user_query

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
        }

        page = requests.get(URL, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        if datetime.now().strftime('%I:%M %p') > '9:30' and datetime.now().strftime('%I:%M %p') < '4:00':
            stockprice = soup.find("span", jsname='vWLAgc').text
            stock = soup.find_all('div', {'class': 'oPhL2e'})[0].find('span').text
            percent = soup.find("span", jsname="rfaVEf").text
            UOD = soup.find("span",jsname="qRSVye").text
            #print(UOD)
            if UOD > "0":
                speak("As of " + datetime.now().strftime('%I:%M %p') + ", " + stock + " is trading at " + stockprice + " $ per share, up " + percent)
            else:
                speak("As of " + datetime.now().strftime('%I:%M %p') + ", " + stock + " is trading at " + stockprice + " $ per share, down " + percent)


            d = datetime.now().date()
            date = str(d.strftime('%w'))
            #print(date)
            if "1" == date:
                if "+" in UOD:
                    speak("As of " + datetime.now().strftime('%I:%M %p') + ", " + stock + " is trading at " + stockprice + " $ per share, up " + percent + " from last friday")
                else:
                    speak("As of " + datetime.now().strftime('%I:%M %p') + ", " + stock + " is trading at " + stockprice + " $ per share, down " + percent)
        else:
            stockprice = soup.find("span", jsname="wurNO").text
            stock = soup.find_all('div', {'class': 'oPhL2e'})[0].find('span').text
            percent = soup.find("span", jsname="sam3Lb").text
            UOD = soup.find("span", jsname="TmYleb").text
            d = datetime.now().date()
            date = str(d.strftime('%w'))
            #print(date)
            if "1" == date:
                if "+" in UOD:
                    speak("As of " + datetime.now().strftime('%I:%M %p') + ", " + stock + " is trading at " + stockprice + " $ per share, up" + percent + " from last friday")
                else:
                    speak("As of " + datetime.now().strftime('%I:%M %p') + ", " + stock + " is trading at " + stockprice + " $ per share, down" + percent + " from last friday")
            else:
                if "+" in UOD:
                    speak("As of " + datetime.now().strftime('%I:%M %p') + ", " + stock + " is trading at " + stockprice + " $ per share, up" + percent + " from yesterday")
                else:
                    speak("As of " + datetime.now().strftime('%I:%M %p') + ", " + stock + " is trading at " + stockprice + " $ per share, down" + percent + " from yesterday")
   except Exception:
        speak("Im sorry, I could not get the price for that stock")
@lru_cache(100)
def spelling(query):
    try:
        user_query = query.replace("search up", "")

        URL = "https://www.google.co.in/search?q=" + user_query

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
        }

        page = requests.get(URL, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        spelling = soup.find(class_='MiCl6d').get_text().replace("·", ",   ")
        s1 = spelling.replace(",   ", "")
        speak(s1 + " is spelled " + spelling)
        print((s1 + " is spelled " + spelling))
        print(s1 + " is spelled " + s1)
    except Exception:  # and result == "" or Exception and result == "":
        speak("Im sorry, I could not find how to spell your word")
def search_query(query):
    try:
        user_query = query.replace("search up", "")

        URL = "https://www.google.co.in/search?q=" + user_query

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
        }

        page = requests.get(URL, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        answer = soup.find(class_='TIGsTb').get_text()
        speak(answer)
        print(answer)
    except Exception:  # and result == "" or Exception and result == "":
        try:

            result = soup.find(class_='di3YZe').get_text()
            print(result.replace("-", " "))
            speak(result.replace("-", " "))
        except Exception:  # and result == "" or Exception and result == "":
            try:
                #
                result = soup.find(class_='kno-rdesc').get_text()
                speak(result.replace("-", " "))
                print(result.replace("-", " "))
            except Exception:
                        try:
                            #
                            result = soup.find(class_='kno-rdesc').get_text()
                            speak(result.replace("-", " "))
                            print(result.replace("-", " "))
                        except Exception:
                            try:
                                #
                                result = soup.find(class_='BbbuR uc9Qxb uE1RRc').get_text()
                                speak(result.replace("-", " "))
                                print(result.replace("-", " "))
                            except Exception:
                                try:
                                    #
                                    result = soup.find(class_='VwiC3b yXK7lf MUxGbd yDYNvb lyLwlc lEBKkf').get_text()
                                    speak(result.replace("-", " "))
                                    print(result.replace("-", " "))
                                except Exception:
                                    print("Sorry, I cant search for that. Please be more clear")
@lru_cache(100)
def read_email(key, value):
    try:
        imapClient = imaplib.IMAP4_SSL(SMTP_SERVER)
        print("\nLogging in...")

        imapClient.login(FROM_EMAIL, FROM_PWD)
        print("\nLog-in successfull!")

        imapClient.select("inbox")
        print("\nReading mailboxes...")

        if (key == None or value == None):
            type, searchResult = imapClient.search(None, "UNSEEN")
            print("\nTotal search emails count:" + str(len(searchResult[0])))

        elif (key != None and value != None):
            type, searchResult = imapClient.search(None, "(" + key + " " + value + ")")
            print("\nTotal search emails count:" + str(len(searchResult[0])))

        for resultCount in searchResult[0].split():
            typ, messages = imapClient.fetch(resultCount, "(RFC822)")

            for message in messages:
                if isinstance(message, tuple):
                    msg = email.message_from_bytes(message[1])
                    email_to_id = msg["to"]
                    email_from_id = msg["from"]
                    email_cc_id = msg["cc"]
                    email_bcc_id = msg["bcc"]
                    email_subject = msg["subject"]
                    email_body = msg["body"]
                    print("\nTo: " + str(email_to_id))
                    print("\nFrom: " + str(email_from_id))
                    print("\nSubject: " + str(email_subject))
                    print("\nBody: " + "".join([part.get_payload() for part in msg.walk()][1]).replace("\r","").replace("\n"," "))
                    speak("\nTo: " + str(email_to_id))
                    speak("\nFrom: " + str(email_from_id))
                    speak("\nSubject: " + str(email_subject))
                    speak(
                        "\nBody: " + "".join([part.get_payload() for part in msg.walk()][1]).replace("\r", "").replace(
                            "\n", " "))

                break

    except Exception as e:
        print("\nException handled: " + str(e))
        print("\nException details:")
        traceback.print_tb(e.__traceback__)
@lru_cache(100)
def calendar():
    service = get_calendar_service()
    # Call the Calendar API
    now = datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
    speak('Getting List of the next 10 events')
    events_result = service.events().list(
        calendarId='primary', timeMin=now,
        maxResults=10, singleEvents=True,
        orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        speak('No upcoming events found.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        speak(start, event['summary'])
@lru_cache(100)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
# Take command function
def take_command():
    start_time = datetime.now()
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        print("recognising")
        query = r.recognize_google(audio, language='en-in')
        end_time = datetime.now()
        print(end_time - start_time)
        print("user said: " + query + "\n")

    except Exception as e:
        print(e)
        print("say that again please...")
        return "None"
    return query
@lru_cache(100)
def send_whatsapp_message(qeury):
    if "dad" in query:
        speak("Whats the message")
        message = take_command()
        speak("Sending message...")
        kit.sendwhatmsg_instantly("+19783056153", message)
        print("Message sent successfully!")
    speak("Who should I text?")
    receiver = take_command()
    if "Dad" in receiver or "dad" in receiver:
        speak("Whats the message")
        message = take_command()
        speak("Sending message...")
        kit.sendwhatmsg_instantly("+19783056153", message)
        print("Message sent successfully!")
@lru_cache(100)
def play_song(song):
    song = song.replace('play', '')
    speak('playing ' + song)
    kit.playonyt(song)
@lru_cache(100)
def wikipedia_search(wiki_query):
    speak("searching in wikipedia..")
    query = wiki_query.replace("tell me about", "")
    results = wikipedia.summary(query, sentences=2)
    speak("according to Wikipedia")
    print(results)
    speak(results)
@lru_cache(100)
def time():
    time = datetime.now().strftime('%I:%M %p')
    speak('Current time is ' + time)
    print('Current time is ' + time)
@lru_cache(100)
def joke():
    joke = pyjokes.get_joke()
    speak(joke)
    print(joke)
@lru_cache(100)
def remember():
    speak("What should I remember")
    print("What should I remember")
    rememberMessage = take_command()
    speak("you said me to remember : " + rememberMessage)
    print("you said me to remember : " + rememberMessage)
    remember = open('data.txt', 'w')
    remember.write(rememberMessage)
    remember.close()
@lru_cache(100)
def recall_remember():
    remember = open('data.txt', 'r')
    speak("you said me to remember that : " + remember.read())
    print("you said me to remember that : " + remember.read())
@lru_cache(100)
def weather(query):
    URL = 'https://www.google.co.in/search?q=' + str(query.replace(" ", "+")) + "/"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
    }

    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    print(soup)
    s1 = soup.find(class_='wob_loc q8U8x').get_text()
    s2 = soup.find(class_='wob_dcp').get_text()
    s3 = soup.find(class_='wob_t q8U8x').get_text()
    speak("In " + s1 + ", its " + s2 + " and its " + s3 + " Degree's fahrenheit")
    print("In " + s1 + ", its " + s2 + " and its " + s3 + " Degree's fahrenheit")
@lru_cache(100)
def send_email():
    speak("Who should I send the message to?")
    to_email = take_command()
    if "dad" in to_email or "Dad" in to_email:
        yag = yagmail.SMTP("thestockdude10@gmail.com", "pqnoalssfcodnous")
        speak("What do you want the subject to be?")
        content_subject = take_command()
        speak("What is the message?")
        content = take_command()
        yag.send('bipulkarki@gmail.com', content_subject, content)
        speak("Email sent sucessfully")
    else:
        speak("Im sorry, I cant sent that email")
@lru_cache(100)
def read_news():
    MSNBC_paper = newspaper.build('https://www.msnbc.com/')
    for article in MSNBC_paper.articles:
        articleurl = article.url
        html = requests.get(articleurl).text
        text = fulltext(html)
        text = text.replace("'", "")
        speak("Here is the latest news")
        print("Here is the latest news")
        print(text)
        speak("Would you like me to read it?")
        print("Would you like me to read it?")
        yN = take_command()
        if "yes" or 'Yes' in yN:
            speak(text)
        else:
            speak("Ok, no problem")
@lru_cache(100)
def math(query):
    try:
        user_query = query.replace("math", "")

        URL = "https://www.google.co.in/search?q=" + user_query

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
        }

        page = requests.get(URL, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        answer = soup.find(class_='XH1CIc').get_text() + soup.find(class_='fB3vD').get_text()
        speak(answer)
        print(answer)
    except Exception:  # and result == "" or Exception and result == "":
        speak("Sorry, I dont have a answer to that math question")
@lru_cache(100)
def definition(query):
        query = query.replace("tell me the definition", "")
        query = query.replace("max", "")
        query = ("definition of " + query)
        client = wolframalpha.Client("32R5H7-G5KG3RU4YQ")
        res = client.query(query)
        output = next(res.results).text
        speak("Here's the definition of " + query)
        print("Here's the definition of " + query)
        print(output)
        speak(output)
if __name__ == "__main__":
    speak("Hello. What can I do")
    global my_timer
    while True:
        query = take_command().lower()
        if 'assistant' in query:
            query = query.replace("assistant", "")
            if "set a timer" in query:
                countdown_thread = threading.Thread(target=countdown, args=[query])
                countdown_thread.start()
            elif 'play' in query:
                play_song(query)
            elif ' time ' in query or " time " in query:
                time()

            elif 'joke' in query:
                joke()
            elif 'search up' in query:
                search_query(query)
            elif 'remember something' in query:
                remember()
            elif 'do you remember anything' in query:
                recall_remember()

            elif "weather" in query:
                if not "search up" in query:
                    weather(query)

            elif "email" in query:
                if not 'read' in query:
                    if 'send' in query:
                        send_email()
            elif "who are you" in query:
                    # if "Max" in query:
                    speak(
                        "I am Quandale dingle, an artificial intellegence made my Sansar Karki. I use manny github repositaries such as Gladiator07/JARVIS, RahulSharma4329's AI-Assistant-Helena, and manny python libraries such as speech reognition, pyttsx3, datetime, wikipedia, pyjokes, pywhatkit, webbrowser, requests and ya-gmail. These libraries allow me to do manny things. ")
                    print(
                        "I am Quandale Dingle, a A.I made for a robot that he plans on making for the 5th grade talent show. I use python and python libraries such asimport speech recognition pyttsx3, datetime, wikipedia, pyjokes, pywhatkit, webbrowser, requests and ya-gmail. I am very smart and can do manny things. I am a prototype of the AI that I will become, but this is the model I will use to code even more features in me.")
            elif "hello" in query or "Hello" in query:
                    # if "Max" in query:
                    speak("Hello. How are you doing")
                    print("Hello. How are you doing")
            elif "questions about you" in query:
                    # if "Max" in query:
                    speak("Ok! I love questions. What are the questions?")
                    print("Ok! I love questions. What are the questions?")
            elif "what can you do" in query:
                    # if "Max" in query:
                    speak(
                        "I can tell you the weather, tell you the news, search somthing up for you, remember stuff, tell you a joke, search something on wikipedia, send a email, play a song on youtube, tell you the time, and more. I will become even smarter as I am coded with even more updates!")
                    print(
                        "I can tell you the weather, tell you the news, search somthing up for you, remember stuff, tell you a joke, search something on wikipedia, send a email, play a song on youtube, tell you the time, and more. I will become even smarter as I am coded with even more updates!")
            elif "you are very smart" in query:
                    # if "Max" in query:
                    speak("thanks, I like compliments. Humans do too.")
                    print("thanks, I like compliments. Humans do too.")
            elif "pause" in query:
                    # if "Max" in query:
                speak("Ok, pausing")
                time.sleep(10)
            elif "news" in query:
                read_news()

            elif "math" in query:
                    if not "search up" in query:
                        math(query)

            elif "tell me the definition of" in query:
                definition(query)
            elif "events on my calendar" in query:
                calendar()

                # elif "make an event" in query:
                # make_a_event()
            elif "read" in query:
                if "email" in query:
                    if not 'send' in query:
                        read_email("3", None)
            elif "text" in query:
                    send_whatsapp_message(query)
            #elif "direction" in query:
            #        speak("What is the origin")
            #        origin = take_command().replace("its", "")
            #        speak("What is the destination")
            #        destination = take_command().replace("its", "")
            #        directions(origin, destination)
            if "spell" in query:
                if not "search up" in query:
                        spelling(query)
            if "stock" in query or "shares" in query or "price in query" in query:
                if not "search up" in query:
                    stock_price(query)
            if "recipe" in query:
                    recipie(query)
            if 'bye' in query:
                    # if "Max" in query:
                    speak(
                        "happy to help, bye bye! And as always, stay true GOOFY AAAAAAHHHHHH UNCLE PRODUCTIONS QUANDALE DINGLEGE CACA PRINGLES DINGDONG")
                    print(
                        "happy to help, bye bye! And as always, stay true GOOFY AAAAAAHHHHHH UNCLE PRODUCTIONS QUANDALE DINGELEGE CACA PRINGLES DINGDONG")
                    exit()