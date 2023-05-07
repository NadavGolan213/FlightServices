import pymongo
from random import choice, randint, random 
from datetime import datetime, timedelta, date
import time


client = pymongo.MongoClient("mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass&directConnection=true&ssl=false")
mydb = client["FlightSevices"]
FlightCol = mydb["Flights"]




#פונקציות מוזרות של איתי
def str_time_prop(start, end, time_format, prop):
    stime = time.mktime(time.strptime(start, time_format))
    etime = time.mktime(time.strptime(end, time_format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(time_format, time.localtime(ptime))


def random_date(start, end):
    string = str_time_prop(start, end, '%m/%d/%Y %I:%M', random()).split(' ')

    date = list(map(int, string[0].split('/')))
    time = list(map(int, string[1].split(':')))

    return datetime(date[2], date[0], date[1], time[0], time[1])

#random_date(start="1/1/2023 1:30", end="1/1/2024 4:50"))



flights = [
    {'Airline': 'ElAl', 'origin' : ('Israel', 'Tel Aviv', 'https://wallpaperaccess.com/full/1893424.jpg') , 'destinations': [('Austria', 'Vienna', 'https://images3.alphacoders.com/111/1112482.jpg'), ('Belarus', 'Minsk' , 'https://wallpapercave.com/wp/wp2307487.jpg'), ('Belgium', 'Brussels','https://wallpaperaccess.com/full/134409.jpg'), ('Brazil', 'São Paulo', 'https://images.alphacoders.com/581/581842.jpg'), ('Bulgaria', 'Sofia', 'https://images4.alphacoders.com/677/677141.jpg'), ('Cyprus', 'Nicosia', 'https://wallpapercave.com/wp/wp2326074.jpg'), ('Czech Republic', 'Prague', 'https://wallpaperaccess.com/full/41215.jpg'), ('Denmark', 'Copenhagen', 'https://images6.alphacoders.com/693/thumb-1920-693237.jpg'), ('France','Paris', 'https://wallpaperaccess.com/full/4063196.jpg' ), ('Germany', 'Berlin', 'https://wallpapercave.com/wp/wp9022131.jpg'), ('United Kingdom', 'London', 'https://wallpaperaccess.com/full/1710773.jpg'), ('Turkey', 'Istanbul', 'https://i.pinimg.com/originals/d9/5e/68/d95e6832254a4bd5974ad2a45d9a6932.jpg'), ('Switzerland', 'Zürich', 'https://images4.alphacoders.com/109/1090279.jpg'), ('Spain', 'Madrid', 'https://wallpaperaccess.com/full/229932.jpg')]},
    {'Airline': 'British Airways', 'origin' : ('United Kingdom', 'London', 'https://wallpaperaccess.com/full/1710773.jpg') , 'destinations': [('Austria', 'Vienna', 'https://images3.alphacoders.com/111/1112482.jpg'), ('Belarus', 'Minsk' , 'https://wallpapercave.com/wp/wp2307487.jpg'), ('Belgium', 'Brussels','https://wallpaperaccess.com/full/134409.jpg'), ('Brazil', 'São Paulo', 'https://images.alphacoders.com/581/581842.jpg'), ('Bulgaria', 'Sofia', 'https://images4.alphacoders.com/677/677141.jpg'), ('Cyprus', 'Nicosia', 'https://wallpapercave.com/wp/wp2326074.jpg'), ('Czech Republic', 'Prague', 'https://wallpaperaccess.com/full/41215.jpg'), ('Denmark', 'Copenhagen', 'https://images6.alphacoders.com/693/thumb-1920-693237.jpg'), ('France','Paris', 'https://wallpaperaccess.com/full/4063196.jpg' ), ('Germany', 'Berlin', 'https://wallpapercave.com/wp/wp9022131.jpg'),  ('Israel', 'Tel Aviv', 'https://wallpaperaccess.com/full/1893424.jpg'), ('Turkey', 'Istanbul', 'https://i.pinimg.com/originals/d9/5e/68/d95e6832254a4bd5974ad2a45d9a6932.jpg'), ('Switzerland', 'Zürich', 'https://images4.alphacoders.com/109/1090279.jpg'), ('Spain', 'Madrid', 'https://wallpaperaccess.com/full/229932.jpg')]},
    {'Airline': 'Turkish Airlines', 'origin' : ('Turkey', 'Istanbul', 'https://i.pinimg.com/originals/d9/5e/68/d95e6832254a4bd5974ad2a45d9a6932.jpg') , 'destinations': [('Austria', 'Vienna', 'https://images3.alphacoders.com/111/1112482.jpg'), ('Belarus', 'Minsk' , 'https://wallpapercave.com/wp/wp2307487.jpg'), ('Belgium', 'Brussels','https://wallpaperaccess.com/full/134409.jpg'), ('Brazil', 'São Paulo', 'https://images.alphacoders.com/581/581842.jpg'), ('Bulgaria', 'Sofia', 'https://images4.alphacoders.com/677/677141.jpg'), ('Cyprus', 'Nicosia', 'https://wallpapercave.com/wp/wp2326074.jpg'), ('Czech Republic', 'Prague', 'https://wallpaperaccess.com/full/41215.jpg'), ('Denmark', 'Copenhagen', 'https://images6.alphacoders.com/693/thumb-1920-693237.jpg'), ('France','Paris', 'https://wallpaperaccess.com/full/4063196.jpg' ), ('Germany', 'Berlin', 'https://wallpapercave.com/wp/wp9022131.jpg'),  ('Israel', 'Tel Aviv', 'https://wallpaperaccess.com/full/1893424.jpg'), ('United Kingdom', 'London', 'https://wallpaperaccess.com/full/1710773.jpg'), ('Switzerland', 'Zürich', 'https://images4.alphacoders.com/109/1090279.jpg'), ('Spain', 'Madrid', 'https://wallpaperaccess.com/full/229932.jpg')]},
    {'Airline': 'Air France', 'origin' : ('France','Paris', 'https://wallpaperaccess.com/full/4063196.jpg' ) , 'destinations': [('Austria', 'Vienna', 'https://images3.alphacoders.com/111/1112482.jpg'), ('Belarus', 'Minsk' , 'https://wallpapercave.com/wp/wp2307487.jpg'), ('Belgium', 'Brussels','https://wallpaperaccess.com/full/134409.jpg'), ('Brazil', 'São Paulo', 'https://images.alphacoders.com/581/581842.jpg'), ('Bulgaria', 'Sofia', 'https://images4.alphacoders.com/677/677141.jpg'), ('Cyprus', 'Nicosia', 'https://wallpapercave.com/wp/wp2326074.jpg'), ('Czech Republic', 'Prague', 'https://wallpaperaccess.com/full/41215.jpg'), ('Denmark', 'Copenhagen', 'https://images6.alphacoders.com/693/thumb-1920-693237.jpg'), ('Turkey', 'Istanbul', 'https://i.pinimg.com/originals/d9/5e/68/d95e6832254a4bd5974ad2a45d9a6932.jpg'), ('Germany', 'Berlin', 'https://wallpapercave.com/wp/wp9022131.jpg'),  ('Israel', 'Tel Aviv', 'https://wallpaperaccess.com/full/1893424.jpg'), ('United Kingdom', 'London', 'https://wallpaperaccess.com/full/1710773.jpg'), ('Switzerland', 'Zürich', 'https://images4.alphacoders.com/109/1090279.jpg'), ('Spain', 'Madrid', 'https://wallpaperaccess.com/full/229932.jpg')]},
    {'Airline': 'Arkia', 'origin' : ('Israel', 'Tel Aviv', 'https://wallpaperaccess.com/full/1893424.jpg') , 'destinations': [('France','Paris', 'https://wallpaperaccess.com/full/4063196.jpg' ), ('Austria', 'Vienna', 'https://images3.alphacoders.com/111/1112482.jpg'), ('Belarus', 'Minsk' , 'https://wallpapercave.com/wp/wp2307487.jpg'), ('Belgium', 'Brussels','https://wallpaperaccess.com/full/134409.jpg'), ('Brazil', 'São Paulo', 'https://images.alphacoders.com/581/581842.jpg'), ('Bulgaria', 'Sofia', 'https://images4.alphacoders.com/677/677141.jpg'), ('Cyprus', 'Nicosia', 'https://wallpapercave.com/wp/wp2326074.jpg'), ('Czech Republic', 'Prague', 'https://wallpaperaccess.com/full/41215.jpg'), ('Denmark', 'Copenhagen', 'https://images6.alphacoders.com/693/thumb-1920-693237.jpg'), ('Turkey', 'Istanbul', 'https://i.pinimg.com/originals/d9/5e/68/d95e6832254a4bd5974ad2a45d9a6932.jpg'), ('Germany', 'Berlin', 'https://wallpapercave.com/wp/wp9022131.jpg'), ('United Kingdom', 'London', 'https://wallpaperaccess.com/full/1710773.jpg'), ('Switzerland', 'Zürich', 'https://images4.alphacoders.com/109/1090279.jpg'), ('Spain', 'Madrid', 'https://wallpaperaccess.com/full/229932.jpg')]},
    {'Airline': 'Austrian Airlines', 'origin' : ('Austria', 'Vienna', 'https://images3.alphacoders.com/111/1112482.jpg') , 'destinations': [('France','Paris', 'https://wallpaperaccess.com/full/4063196.jpg' ), ('Belarus', 'Minsk' , 'https://wallpapercave.com/wp/wp2307487.jpg'), ('Belgium', 'Brussels','https://wallpaperaccess.com/full/134409.jpg'), ('Brazil', 'São Paulo', 'https://images.alphacoders.com/581/581842.jpg'), ('Bulgaria', 'Sofia', 'https://images4.alphacoders.com/677/677141.jpg'), ('Cyprus', 'Nicosia', 'https://wallpapercave.com/wp/wp2326074.jpg'), ('Czech Republic', 'Prague', 'https://wallpaperaccess.com/full/41215.jpg'), ('Denmark', 'Copenhagen', 'https://images6.alphacoders.com/693/thumb-1920-693237.jpg'), ('Turkey', 'Istanbul', 'https://i.pinimg.com/originals/d9/5e/68/d95e6832254a4bd5974ad2a45d9a6932.jpg'), ('Germany', 'Berlin', 'https://wallpapercave.com/wp/wp9022131.jpg'),  ('Israel', 'Tel Aviv', 'https://wallpaperaccess.com/full/1893424.jpg'), ('United Kingdom', 'London', 'https://wallpaperaccess.com/full/1710773.jpg'), ('Switzerland', 'Zürich', 'https://images4.alphacoders.com/109/1090279.jpg'), ('Spain', 'Madrid', 'https://wallpaperaccess.com/full/229932.jpg')]},
    {'Airline': 'Swiss International Air Lines', 'origin' : ('Switzerland', 'Zürich', 'https://images4.alphacoders.com/109/1090279.jpg') , 'destinations': [('Austria', 'Vienna', 'https://images3.alphacoders.com/111/1112482.jpg'), ('France','Paris', 'https://wallpaperaccess.com/full/4063196.jpg' ), ('Belarus', 'Minsk' , 'https://wallpapercave.com/wp/wp2307487.jpg'), ('Belgium', 'Brussels','https://wallpaperaccess.com/full/134409.jpg'), ('Brazil', 'São Paulo', 'https://images.alphacoders.com/581/581842.jpg'), ('Bulgaria', 'Sofia', 'https://images4.alphacoders.com/677/677141.jpg'), ('Cyprus', 'Nicosia', 'https://wallpapercave.com/wp/wp2326074.jpg'), ('Czech Republic', 'Prague', 'https://wallpaperaccess.com/full/41215.jpg'), ('Denmark', 'Copenhagen', 'https://images6.alphacoders.com/693/thumb-1920-693237.jpg'), ('Turkey', 'Istanbul', 'https://i.pinimg.com/originals/d9/5e/68/d95e6832254a4bd5974ad2a45d9a6932.jpg'), ('Germany', 'Berlin', 'https://wallpapercave.com/wp/wp9022131.jpg'),  ('Israel', 'Tel Aviv', 'https://wallpaperaccess.com/full/1893424.jpg'), ('United Kingdom', 'London', 'https://wallpaperaccess.com/full/1710773.jpg'), ('Spain', 'Madrid', 'https://wallpaperaccess.com/full/229932.jpg')]},
    {'Airline': 'Iberia', 'origin' : ('Spain', 'Madrid', 'https://wallpaperaccess.com/full/229932.jpg') , 'destinations': [('Switzerland', 'Zürich', 'https://images4.alphacoders.com/109/1090279.jpg'),('Austria', 'Vienna', 'https://images3.alphacoders.com/111/1112482.jpg'), ('France','Paris', 'https://wallpaperaccess.com/full/4063196.jpg' ), ('Belarus', 'Minsk' , 'https://wallpapercave.com/wp/wp2307487.jpg'), ('Belgium', 'Brussels','https://wallpaperaccess.com/full/134409.jpg'), ('Brazil', 'São Paulo', 'https://images.alphacoders.com/581/581842.jpg'), ('Bulgaria', 'Sofia', 'https://images4.alphacoders.com/677/677141.jpg'), ('Cyprus', 'Nicosia', 'https://wallpapercave.com/wp/wp2326074.jpg'), ('Czech Republic', 'Prague', 'https://wallpaperaccess.com/full/41215.jpg'), ('Denmark', 'Copenhagen', 'https://images6.alphacoders.com/693/thumb-1920-693237.jpg'), ('Turkey', 'Istanbul', 'https://i.pinimg.com/originals/d9/5e/68/d95e6832254a4bd5974ad2a45d9a6932.jpg'), ('Germany', 'Berlin', 'https://wallpapercave.com/wp/wp9022131.jpg'),  ('Israel', 'Tel Aviv', 'https://wallpaperaccess.com/full/1893424.jpg'), ('United Kingdom', 'London', 'https://wallpaperaccess.com/full/1710773.jpg')]},
    ]



def create_flights():

    AirlinesflightsNum = 10

    for AirLine in flights:
        AirLineName = AirLine['Airline']
        origin = AirLine['origin']
        destinations = AirLine['destinations']

        for destination in destinations:
            
            #today = date.today()
            now = datetime.now()
            twoweeks = now + timedelta(weeks=2) 

            today = now.strftime("%m/%d/%Y %I:%M")
            end = twoweeks.strftime("%m/%d/%Y %I:%M")

            FlightDate1 = random_date(start= today, end= end)#בין התאריכים
            FlightDuration1 = timedelta(hours= randint(3, 12)) 
            ArivingDate1 = FlightDate1 + FlightDuration1 

            FlightDate2 = random_date(start=today, end= end) #בין התאריכים
            FlightDuration2 = timedelta(hours= randint(3, 12))
            ArivingDate2 = FlightDate2 + FlightDuration2 

            new_flight1 = {'Airline': AirLineName, 'origin': origin, 'destinations': destination, 'FlightDate': FlightDate1.strftime("%m/%d/%Y %I:%M"), 'FlightDuration': FlightDuration1.__str__(), 'ArivingDate': ArivingDate1.strftime("%m/%d/%Y %I:%M"), 'price': randint(150, 1200)}
            new_flight2 = {'Airline': AirLineName, 'origin': destination, 'destinations': origin, 'FlightDate': FlightDate2.strftime("%m/%d/%Y %I:%M"), 'FlightDuration': FlightDuration2.__str__(), 'ArivingDate': ArivingDate2.strftime("%m/%d/%Y %I:%M"), 'price': randint(150, 1200)}

            FlightCol.insert_one(new_flight1)
            FlightCol.insert_one(new_flight2)

            

#random destination from the list
#לעשות תאריך לשבועיים הרקרובים, לשנות את מספר הטיסות לחברה


def recreate():
    FlightCol.delete_many({})
    create_flights()


