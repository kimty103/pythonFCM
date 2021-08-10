import requests
import json
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

#connect to firebase database
cred = credentials.Certificate("fcmtestapp-fa37a-firebase-adminsdk-bl6rk-25f18c94c8.json") #key file name
firebase_admin.initialize_app(cred)

db = firestore.client()

#preprocess to send push message
url = "https://fcm.googleapis.com/fcm/send"

headers = {
  'Authorization': 'key=AAAA6FaIh8s:APA91bHW4Bcs5iwJeKiL-bbVPJlJUvO-4efm5pW1IOWDGmoFH9exok5-nPNyFQn6SHiMRnLrWrWFvyNJ_BMNNEbrxyzBJYmeOPzHGjX41vEaC_YoLvUkRLysqbJku2iHt4-Lfl51lT5n', # key value of firebase project
  'Content-Type': 'application/json'
}

getValue = 0
while(1):
    getValue = int(input())   #get input value(this maybe a sensor value)
 #   print(getValue)
    if(getValue == 1):
        users_ref = db.collection(u'users')
        docs = users_ref.stream()
        for doc in docs:
            #print(f'{doc.id} => {(doc.to_dict())["token"]}')
            #print((doc.to_dict()))
            msg = "your floor is " + str((doc.to_dict())["floor"])
            payload = json.dumps({
              "to": (doc.to_dict())["token"],
              "notification": {
                "title": "Python",
                "body": msg
              }
            })
            response = requests.request("POST", url, headers=headers, data=payload)
            print(response.text)

        print(type(docs))
    elif(getValue == -1):
        break

