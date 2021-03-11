from django.shortcuts import render
import pyrebase
from django.contrib import auth

config = {
    'apiKey': "AIzaSyBi4GyAJruQHfIxdUZtrAZhJnn60vmmOmU",
    'databaseURL': " https://majorproject-1e1cc-default-rtdb.firebaseio.com",
    'authDomain': "majorproject-1e1cc.firebaseapp.com",
    'projectId': "majorproject-1e1cc",
    'storageBucket': "majorproject-1e1cc.appspot.com",
    'messagingSenderId': "298116078927",
    'appId': "1:298116078927:web:36456eb8a336f725adb93a",
    'measurementId': "G-0BJMZN25D6"
}
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
database = firebase.database()


def login(request):
    return render(request, 'login.html')


def postsign(request):
    email = request.POST.get('Username')
    password = request.POST.get('Password')
    try:
        user = auth.sign_in_with_email_and_password(email, password)
    except:
        message = "Invalid Credentials"
        return render(request, "login.html", {"message": message})
    print(email, password)
    session_id = user['idToken']
    request.session['uid'] = str(session_id)
    return render(request, 'events.html', {"email": email})


def signup(request):
    return render(request, 'signup.html')


def postsignup(request):
    email = request.POST.get("Username")
    password = request.POST.get("Password")
    print(email, password)
    try:
        user = authe.create_user_with_email_and_password(email, password)
    except Exception as e:
        print(e)
        message = "couldn't create"
        return render(request, 'signup.html', {'message': message})
    """ print("Hello")
    uid = user['localId']
    data = {'phone_no':phone_no,'status':'1'}
    try:
        database.child("users").child(uid).child("details").set(data)
    except Exception as e:
        print(e)
        return render(request,'signup.html')"""
    return render(request, 'login.html')
