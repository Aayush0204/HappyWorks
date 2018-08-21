#REST API + FIREBASE
#src="https://www.gstatic.com/firebasejs/5.4.0/firebase.js"

#Initialize Firebase
# config = {
# "apiKey": "AIzaSyD_Tx3x9_Qid04w-nNsICeFDH3_lpfheFs",
# "authDomain": "happyworks-9db2e.firebaseapp.com",
# "databaseURL": "https://happyworks-9db2e.firebaseio.com",
# "projectId": "happyworks-9db2e",
# "storageBucket": "happyworks-9db2e.appspot.com",
# "messagingSenderId": "90914705848"
# }
from firebase import firebase
from flask import Flask,request,Response
import json

url="https://happyworks-9db2e.firebaseio.com"

application = Flask(__name__)

firebase=firebase.FirebaseApplication(url,None) #connect to firebase database
#result=firebase.get('/Questions',None)
@application.route("/create_questions",methods=['POST'])
def create_questions():

    incomming_data=request.data
    
    resultQue= firebase.post('/Questions',{'A':'Ans1','B':'ans2','C':'ans3','Question':'What is my name'})
    print(resultQue)

    response_body = 'Question created in FIREBASE'
    return Response(
            response_body,
            status=200
        )

if __name__ == '__main__':
    logging.info('Application is started...')
    application.run()