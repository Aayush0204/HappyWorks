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
#from flask import Flask
url="https://happyworks-9db2e.firebaseio.com"
firebase=firebase.FirebaseApplication(url,None)
#result=firebase.get('/Questions',None)
resultQue= firebase.post('/Questions',{'A':'Ans1','B':'ans2','C':'ans3','Question':'What is my name'})
print(resultQue)
