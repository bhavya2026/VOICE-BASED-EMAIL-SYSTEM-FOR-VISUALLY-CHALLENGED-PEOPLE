import smtplib 
import speech_recognition as sr
import pyttsx3 
from email.message import EmailMessage

listener = sr.Recognizer()
engine = pyttsx3.init()

def talk(text): 
    engine.say(text)
    engine.runAndWait()


def get_info():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)# captures human voice
            info = listener.recognize_google(voice)# convert human voice to text
            print(info)
            return info.lower()# convert the human speech into lower case text
    except:
        pass


def send_email(receiver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)# creates a server between sender and reciever
    server.starttls()
    server.login('infotuber64@gmail.com', '9996680452')# takes senders email and password as parameters
    email = EmailMessage()
    email['From'] = 'infotuber64@gmail.com'
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)# this method is use to take message as input/parameter to be send
    server.send_message(email)

#this list has been created for user profits,as the key name is called or captured by the system ,the corresponding email address will be reflected
email_list = {
    'bhavya': 'bhavyasrivastava2026@gmail.com',
    'sakshi': 'goyalsakshi7200@gmail.com'
}


def get_email_info():
    talk('To Whom you want to send email')# the function talk is invoked
    name = get_info()#the func get_info is called
    receiver = email_list[name]
    print(receiver)
    talk('What is the subject of your email?')
    subject = get_info()
    talk('Tell me the text in your email')
    message = get_info()
    send_email(receiver, subject, message)
    talk('Hey lazy man. Your email is sent')
    talk('Do you want to send more email?')
    send_more = get_info()# to send the mails again and again
    if 'yes' in send_more:
        get_email_info()

get_email_info()