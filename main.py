from contextlib import nullcontext
from flask import Flask, render_template, request, redirect
from flight import flights
from models import User
import CreateFlights
import pymongo
import random
from random import choice
from datetime import datetime, timedelta, date
import time
from user import User
from pprint import pprint

CreateFlights.recreate()

app = Flask(__name__)
objectuser = None

#db
client = pymongo.MongoClient("mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass&directConnection=true&ssl=false")

mydb = client["FlightSevices"]
UserCol = mydb["Users"]
FlightCol = mydb["Flights"]


#routes
@app.route('/user/signup', methods = ['GET', 'POST'])
def signup_page():
    if (request.method == "POST"):
        userFname = request.form["fName"]
        userLname = request.form["lName"]
        userNickname = request.form["username"]
        userEmail = request.form["email"]
        userPass = request.form["password"]

        y = 0

        for x in UserCol.find({"email": userEmail}):
            y+=1

        if (y == 0):
            
            id = UserCol.insert_one({"fName" :  userFname, "lName": userLname, "userName": userNickname , "email": userEmail, "password": userPass, "gender": "", "age": "", "profliePic": "", "country": "", "adress": ""})

            global objectuser
            objectuser = User(id, userFname, userLname, userNickname, userEmail, userPass, '', '', '', '', '', '')

            print (objectuser)
            pprint(vars(objectuser))

            return redirect("/user/profile")
    

    else:
        return render_template('signUp.html')

    

@app.route('/user/signin', methods = ['GET', 'POST'])
def signin_page():
    if(request.method == "POST"):
        userNickname = request.form["name"]
        userEmail = request.form["email"]
        userPass = request.form["password"]

        y = 0

        for x in UserCol.find({"email": userEmail, "password": userPass}):
            y+=1

        if (y != 0):

            user = UserCol.find_one({"email": userEmail, "password": userPass})
            global objectuser
            objectuser = User(user['_id'], user['fName'], user['lName'], user['userName'], user['email'], user['password'], '', '', '', '', '', '')

            print (objectuser)
            return redirect("/user/uneditedprofile")
        
    return render_template('signIn.html')
 
 

@app.route('/user/profile', methods = ['GET', 'POST'])
def profile_page():
    
    if (request.method == "POST"):
        usergender = request.form["gender"]
        userage = request.form["age"]
        userstate = request.form["state"]
        usercity = request.form["city"]
        userstreet = request.form["street"]
        userPostcode = request.form["Postcode"]

        objectuser.gender = usergender 
        objectuser.age = userage
        objectuser.state = userstate
        objectuser.city = usercity
        objectuser.street = userstreet
        objectuser.postcode = userPostcode

        print(objectuser)
        print("ffesf")
        pprint(vars(objectuser))


        newvalues = { "$set": { "gender": usergender, "age": userage, "profliePic": objectuser.photo, "city": usercity, "state": userstate, "street": userstreet, "postcode": userPostcode} }
        print(newvalues)

    
        user = UserCol.find_one({"email": objectuser.email})

        print("before")
        UserCol.update_one(user, newvalues)
        print("after")
        pprint(vars(objectuser))

        return redirect("/user/uneditedprofile")
        
        
    print ("in profile else ")

    return render_template('profile.html', objectuser = objectuser, logged = objectuser != None, userName = "" if objectuser == None else objectuser.userName )

@app.route('/user/uneditedprofile')
def uneditedprofile_page():
 return render_template('uneditprofile.html', objectuser = objectuser, logged = objectuser != None, userName = "" if objectuser == None else objectuser.userName )

@app.route("/")
@app.route("/home")
def home_page():
    return render_template('home.html', logged = objectuser != None, userName = "" if objectuser == None else objectuser.userName)


#flight data 
#פונקציות 
def findflight(origin ,destination, flightDate):

    objectFlightList = []

    strflightdate = datetime.strptime(flightDate, '%m/%d/%Y %I:%M')
    myquery = {'origin': [origin], 'destination': [destination], 'FlightDate' : strflightdate} #?לא יעבוד
    flist = FlightCol.find(myquery)
    
    
    for flight in flist:
        objectflight = flights(flight['_id'], flight['Airline'], flight['origin'], flight['destinations'], datetime.strptime(flight['FlightDate'], '%m/%d/%Y %I:%M'), datetime.strptime(flight['FlightDuration'], '%H:%M:%S', ), datetime.strptime(flight['ArivingDate'], '%m/%d/%Y %I:%M'), flight['price'])

        objectFlightList.append(objectflight)
    
    return objectFlightList

def findflightbyorigin(origin):

    objectFlightList = []

    arrorigin = None

    for flight in allflights():

        for Origin in flight.origin:
            if(origin in Origin):
                arrorigin = Origin 

    if(arrorigin == None): return objectFlightList


    myquery = {'origin': arrorigin} #?לא יעבוד
    flist = FlightCol.find(myquery)
    
    
    for flight in flist:
       
        objectflight = flights(flight['_id'], flight['Airline'], flight['origin'], flight['destinations'], datetime.strptime(flight['FlightDate'], '%m/%d/%Y %I:%M'), datetime.strptime(flight['FlightDuration'], '%H:%M:%S', ), datetime.strptime(flight['ArivingDate'], '%m/%d/%Y %I:%M'), flight['price'])
        objectFlightList.append(objectflight)
        #pprint(vars(objectflight))

        #print(flight['time'], flight['origin'])
    
    
    #pprint(vars(objectFlightList))
    
    return objectFlightList


def findflightbydestination(destination):

    objectFlightList = []

    arrdestination = None

    for flight in allflights():

        for Destinations in flight.destinations:
            if(destination in Destinations):
                arrdestination = Destinations 

    if(arrdestination == None): return objectFlightList


    myquery = {'destinations': arrdestination} #?לא יעבוד
    flist = FlightCol.find(myquery)
    
    
    for flight in flist:
       
        objectflight = flights(flight['_id'], flight['Airline'], flight['origin'], flight['destinations'], datetime.strptime(flight['FlightDate'], '%m/%d/%Y %I:%M'), datetime.strptime(flight['FlightDuration'], '%H:%M:%S', ), datetime.strptime(flight['ArivingDate'], '%m/%d/%Y %I:%M'), flight['price'])
        objectFlightList.append(objectflight)
        #pprint(vars(objectflight))

        #print(flight['time'], flight['origin'])
    
    
    #pprint(vars(objectFlightList))
    
    return objectFlightList

def findflightbyorigindestination(origin ,destination):

    objectFlightList = []

    arrdestination = None
    arrorigin = None

    for flight in allflights():

        for Origin in flight.origin:
            if(origin in Origin):
                arrorigin = Origin 


    for flight in allflights():

        for Destinations in flight.destinations:
            if(destination in Destinations):
                arrdestination = Destinations 

    if(arrdestination == None or arrorigin == None): return objectFlightList


    myquery = {'origin': arrorigin, 'destinations': arrdestination} #?לא יעבוד
    flist = FlightCol.find(myquery)
    
    
    for flight in flist:
        objectflight = flights(flight['_id'], flight['Airline'], flight['origin'], flight['destinations'], datetime.strptime(flight['FlightDate'], '%m/%d/%Y %I:%M'), datetime.strptime(flight['FlightDuration'], '%H:%M:%S', ), datetime.strptime(flight['ArivingDate'], '%m/%d/%Y %I:%M'), flight['price'])

        objectFlightList.append(objectflight)
    
    return objectFlightList

def findflightbyflightDate(flightDate):

    objectFlightList = []

    strflightdate = datetime.strptime(flightDate, '%m/%d/%Y %I:%M')

    myquery = {'flightDate': strflightdate} #?לא יעבוד
    flist = FlightCol.find(myquery)
    
    
    for flight in flist:
        objectflight = flights(flight['_id'], flight['Airline'], flight['origin'], flight['destinations'], datetime.strptime(flight['FlightDate'], '%m/%d/%Y %I:%M'), datetime.strptime(flight['FlightDuration'], '%H:%M:%S', ), datetime.strptime(flight['ArivingDate'], '%m/%d/%Y %I:%M'), flight['price'])

        objectFlightList.append(objectflight)
    
    return objectFlightList
    
def findflightbyflightDateOrigin(flightDate, origin):

    objectFlightList = []

    strflightdate = datetime.strptime(flightDate, '%m/%d/%Y %I:%M')

    arrorigin = None

    for flight in allflights():

        for Origin in flight.origin:
            if(origin in Origin):
                arrorigin = Origin 

    if(arrorigin == None): return objectFlightList


    myquery = {'flightDate': strflightdate, 'origin': arrorigin} #?לא יעבוד
    flist = FlightCol.find(myquery)
    
    
    for flight in flist:
        objectflight = flights(flight['_id'], flight['Airline'], flight['origin'], flight['destinations'], datetime.strptime(flight['FlightDate'], '%m/%d/%Y %I:%M'), datetime.strptime(flight['FlightDuration'], '%H:%M:%S', ), datetime.strptime(flight['ArivingDate'], '%m/%d/%Y %I:%M'), flight['price'])

        objectFlightList.append(objectflight)
    
    return objectFlightList


def findflightbyflightDateDestination(flightDate, destination):

    objectFlightList = []

    strflightdate = datetime.strptime(flightDate, '%m/%d/%Y %I:%M')

    myquery = {'flightDate': strflightdate, 'destination': [destination]} #?לא יעבוד
    flist = FlightCol.find(myquery)
    
    
    for flight in flist:
        objectflight = flights(flight['_id'], flight['Airline'], flight['origin'], flight['destinations'], datetime.strptime(flight['FlightDate'], '%m/%d/%Y %I:%M'), datetime.strptime(flight['FlightDuration'], '%H:%M:%S', ), datetime.strptime(flight['ArivingDate'], '%m/%d/%Y %I:%M'), flight['price'])

        objectFlightList.append(objectflight)
    
    return objectFlightList

def allflights():

    objectFlightList = []

    flist = FlightCol.find()
    
    
    for flight in flist:
        objectflight = flights(flight['_id'], flight['Airline'], flight['origin'], flight['destinations'], datetime.strptime(flight['FlightDate'], '%m/%d/%Y %I:%M'), datetime.strptime(flight['FlightDuration'], '%H:%M:%S', ), datetime.strptime(flight['ArivingDate'], '%m/%d/%Y %I:%M'), flight['price'])

        objectFlightList.append(objectflight)
    
    return objectFlightList



@app.route('/flightMarket', methods = ['GET', 'POST'])
def market_page():
    if (request.method == "POST"):

        print("in post")
        
        
        origin = request.form["origin"]
        print("origin", origin)
        destination = request.form["destination"]
        print("destination", destination)

        flightdate = request.form["flightdate"]
        print("flightdate", flightdate)
        ticketsnum = request.form["ticketsnum"]
        print("ticketsnum", ticketsnum)
    
        if(origin == '' and destination == ''):
            print("4")
            objectFlightList = findflightbyflightDate(flightdate)
        elif(origin == '' and flightdate == ''):
            print("5")
            objectFlightList = findflightbydestination(destination)
        elif(destination == '' and flightdate == ''):
            print("elif(not destination and not flightdate):")
            objectFlightList = findflightbyorigin(origin)
            print("after fun")
        elif (origin == ''):
           print("1") 
           objectFlightList = findflightbyflightDateDestination(destination, flightdate )
        elif (destination == ''):
            print("2")
            objectFlightList = findflightbyflightDateOrigin(origin, flightdate)
        elif(flightdate == ''):
            print("3")
            objectFlightList = findflightbyorigindestination(origin, destination)
        else :
            print("else")
            objectFlightList = findflight(origin, destination, flightdate)
        
        print(objectFlightList)
        return render_template('flightMarket.html', objectFlightList = objectFlightList, logged = objectuser != None, userName = "" if objectuser == None else objectuser.userName)
    
    else : 
        return render_template('flightMarket.html', objectFlightList = allflights(), logged = objectuser != None, userName = "" if objectuser == None else objectuser.userName)
 #to change to error page

   

   


#@app.route('/about/<username>')
#def about_page(username):
#    return '<h1>this is the about page of {username}</h1>'
app.run(debug=True)
