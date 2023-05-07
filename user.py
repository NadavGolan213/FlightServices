class User:
    
    def __init__(self, id ,fName, lName, userName, email, password, gender, age, state , city, street, Postcode):
        self.id = id
        self.fName = fName
        self.lName = lName
        self.userName = userName
        self.email = email 
        self.password = password 
        self.gender = gender
        self.age = age

        self.state = state
        #adress:
        self.city = city
        self.street = street
        self.postcode = Postcode
        
        if(gender == "male"):
            self.photo = "https://st3.depositphotos.com/15648834/17930/v/600/depositphotos_179308454-stock-illustration-unknown-person-silhouette-glasses-profile.jpg"
        else:
            self.photo = "https://media.istockphoto.com/vectors/brown-hair-woman-face-avatar-happy-girl-faceless-male-cartoon-flat-vector-id1133973476?k=20&m=1133973476&s=170667a&w=0&h=zO5VXHa12Nf3P5rdpTqxGObmR59Az5ahxAOFYgOq-Xk="



    







'''
   #get functions
    def GetAirline(self):
        return self.id
    def GetAirline(self):
        return self.Airline
    def GetAirline(self):
        return self.origin
    def GetAirline(self):
        return self.destinations
    def GetAirline(self):
        return self.FlightDate
    def GetAirline(self):
        return self.FlightDuration
    def GetAirline(self):
        return self.ArivingDate
    def GetAirline(self):
        return self.price
'''
