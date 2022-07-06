# THE PYTHON CODE FOR THE MOVIE TICKET BOOKING SYSTEM

import re

class Account:
    def __init__(self, name, age, sex, dob, phoneno, email, nationality):
        self.name = name
        self.age = age
        self.sex = sex
        self.dob = dob
        self.phoneno = phoneno
        self.email = email
        self.nationality = nationality

class Ticket:
    def __init__(self, price, totalp):
        self.price = price
        self.totalp = totalp

class Movie:
    def __init__(self, movieName, movieDay, movieTime, movieCenter, movieScreen, movieSeats):
        self.movieName =  movieName
        self.movieDay = movieDay
        self.movieTime = movieTime
        self.movieCenter = movieCenter
        self.movieScreen = movieScreen
        self.movieSeats = movieSeats

def Theater():
    Ticket.price = Ticket.price + 150
    tP = ["Screen 1", "Screen 2", "Screen 3", "Screen 4", "Screen 5"]
    print("\nChoose the movie of your choice:\n")
    print("1 --->", tP[0])
    print("2 --->", tP[1])
    print("3 --->", tP[2])
    print("4 --->", tP[3])
    print("5 --->", tP[4])
    print("\nOR Press 6 to go back:")
    screen = int(input(">> "))
    if screen == 1:
        Movie.movieScreen = tP[0]
        print("\nYour selected Screen is: ", Movie.movieScreen)
        print("\nDo you want to continue? ")
        ch = int(input("Press 1 to Continue or 2 to go back: "))
        if ch == 1:
            chooseTimings()
        elif ch == 2:
            Theater()
    elif screen == 2:
        Movie.movieScreen = tP[1]
        print("\nYour selected Screen is: ", Movie.movieScreen)
        print("\nDo you want to continue? ")
        ch = int(input("Press 1 to Continue or 2 to go back: "))
        if ch == 1:
            chooseTimings()
        elif ch == 2:
            Theater()
    elif screen == 3:
        Movie.movieScreen = tP[2]
        print("\nYour selected Screen is: ", Movie.movieScreen)
        print("\nDo you want to continue? ")
        ch = int(input("Press 1 to Continue or 2 to go back: "))
        if ch == 1:
            chooseTimings()
        elif ch == 2:
            Theater()
    elif screen == 4:
        Movie.movieScreen = tP[3]
        print("\nYour selected Screen is: ", Movie.movieScreen)
        print("\nDo you want to continue? ")
        ch = int(input("Press 1 to Continue or 2 to go back: "))
        if ch == 1:
            chooseTimings()
        elif ch == 2:
            Theater()
    elif screen == 5:
        Movie.movieScreen = tP[3]
        print("\nYour selected Screen is: ", Movie.movieScreen)
        print("\nDo you want to continue? ")
        ch = int(input("Press 1 to Continue or 2 to go back: "))
        if ch == 1:
            chooseTimings()
        elif ch == 2:
            Theater()                               
    elif screen == 6:
        chooseCenter()
    else:
        print("\n✖ PLEASE ENTER A VALID CHOICE!")
        Theater()          
    return 0    

def TheaterM():
    Ticket.price = Ticket.price + 300
    tP = ["Screen 1", "Screen 2", "Screen 3", "Screen 4"]
    print("\nChoose the movie of your choice:\n")
    print("1 --->", tP[0])
    print("2 --->", tP[1])
    print("3 --->", tP[2])
    print("4 --->", tP[3])
    print("\nOR Press 5 to go back:")
    screenM = int(input(">> "))
    if screenM == 1:
        Movie.movieScreen = tP[0]
        print("\nYour selected Screen is: ", Movie.movieScreen)
        print("\nDo you want to continue? ")
        ch = int(input("Press 1 to Continue or 2 to go back: "))
        if ch == 1:
            chooseTimings2()
        elif ch == 2:
            TheaterM()
    elif screenM == 2:
        Movie.movieScreen = tP[1]
        print("\nYour selected Screen is: ", Movie.movieScreen)
        print("\nDo you want to continue? ")
        ch = int(input("Press 1 to Continue or 2 to go back: "))
        if ch == 1:
            chooseTimings2()
        elif ch == 2:
            TheaterM()
    elif screenM == 3:
        Movie.movieScreen = tP[2]
        print("\nYour selected Screen is: ", Movie.movieScreen)
        print("\nDo you want to continue? ")
        ch = int(input("Press 1 to Continue or 2 to go back: "))
        if ch == 1:
            chooseTimings2()
        elif ch == 2:
            TheaterM()
    elif screenM == 4:
        Movie.movieScreen = tP[3]
        print("\nYour selected Screen is: ", Movie.movieScreen)
        print("\nDo you want to continue? ")
        ch = int(input("Press 1 to Continue or 2 to go back: "))
        if ch == 1:
            chooseTimings2()
        elif ch == 2:
            TheaterM()                     
    elif screenM == 5:
        chooseCenter()
    else:
        print("\n✖ PLEASE ENTER A VALID CHOICE!")
        TheaterM()          
    return 0    

def TheaterX():
    Ticket.price = Ticket.price + 400
    tP = ["Screen 1", "Screen 2", "Screen 3"]
    print("\nChoose the movie of your choice:\n")
    print("1 --->", tP[0])
    print("2 --->", tP[1])
    print("3 --->", tP[2])
    print("\nOR Press 4 to go back:")
    screenX = int(input(">> "))
    if screenX == 1:
        Movie.movieScreen = tP[0]
        print("\nYour selected Screen is: ", Movie.movieScreen)
        print("\nDo you want to continue? ")
        ch = int(input("Press 1 to Continue or 2 to go back: "))
        if ch == 1:
            chooseTimings3()
        elif ch == 2:
            TheaterX()
    elif screenX == 2:
        Movie.movieScreen = tP[1]
        print("\nYour selected Screen is: ", Movie.movieScreen)
        print("\nDo you want to continue? ")
        ch = int(input("Press 1 to Continue or 2 to go back: "))
        if ch == 1:
            chooseTimings3()
        elif ch == 2:
            TheaterX()
    elif screenX == 3:
        Movie.movieScreen = tP[2]
        print("\nYour selected Screen is: ", Movie.movieScreen)
        print("\nDo you want to continue? ")
        ch = int(input("Press 1 to Continue or 2 to go back: "))
        if ch == 1:
            chooseTimings3()
        elif ch == 2:
            TheaterX()       
    elif screenX == 4:
        chooseCenter()
    else:
        print("\n✖ PLEASE ENTER A VALID CHOICE!")
        TheaterX()          
    return 0    

def chooseNoOfSeats():
    Movie.movieSeats = int(input("\nChoose the number of seats you want: "))
    print("Number of tickets to be generated:-", Movie.movieSeats)
    Ticket.totalp = (Ticket.price * Movie.movieSeats)
    pp = (Ticket.totalp // Movie.movieSeats)
    print("Ticket price(Per Person): ₹", pp)
    print("The total price for your tickets are: ₹", Ticket.totalp)
    cs = int(input("Do you want to Continue? Press 1 to continue or 2 to go back: "))
    if cs == 1:
        print("\n✔ TICKETS BOOKED SUCCESSFULLY!! ✔")
        generateBill()
    elif cs == 2:
        chooseNoOfSeats()

def generateBill():
    print("\n\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("\t*   Name                   :  ", Account.name)
    print("\t*   Phone number           :  ", Account.phoneno)
    print("\t*   Movie                  :  ", Movie.movieName)
    print("\t*   Theater                :  ", Movie.movieCenter)
    print("\t*   Screen                 :  ", Movie.movieScreen)
    print("\t*   Number of seats chosen :  ", Movie.movieSeats)
    print("\t*   Day of Movie           :  ", Movie.movieDay)
    print("\t*   Timing for the movie   :  ", Movie.movieTime)
    print("\t*   Grand Total            : ₹", Ticket.totalp)
    print("\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("\nDo you want to create another order? ")
    ja = input("yes or no: ").lower()
    if ja == "yes":
        showAccDetails2()
    else:
        print("\nThanks for booking with us :) ")
        print("\nHAVE A NICE DAY AHEAD!!\n")
        exit()

def accDetails2():
    Account.name = input("\nPlease Enter your Name >> ")
    Account.age = int(input("Please Enter your Age >> "))
    g = input("Please Enter your Sex (M/F/O) >> ").upper()
    if g == "M":
        Account.sex = g
        Account.phoneno = int(input("Please Enter your Phone number >> "))
        print("Please Enter your Email ID: ")
        iemail = input()
        Account.email = re.findall(r'([a-zA-Z0-9+._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+)', iemail)
        print("Please Enter your Date of Birth: ")
        idob = input("(in dd/mm/yyyy format) ")
        Account.dob = re.findall(r'\d{2}[/]\d{2}[/]\d{4}', idob)
        Account.nationality = input("Please enter your Nationality: ")
        showaccDetails()
        return 0
    elif g == "F":
        Account.sex = g
        Account.phoneno = int(input("Please Enter your Phone number >> "))
        print("Please Enter your Email ID: ")
        iemail = input()
        Account.email = re.findall(r'([a-zA-Z0-9+._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+)', iemail)
        print("Please Enter your Date of Birth: ")
        idob = input("(in dd/mm/yyyy format) ")
        Account.dob = re.findall(r'\d{2}[/]\d{2}[/]\d{4}', idob)
        Account.nationality = input("Please enter your Nationality: ")
        showaccDetails()
        return 0
    elif g == "O":
        Account.sex = g
        Account.phoneno = int(input("Please Enter your Phone number >> "))
        print("Please Enter your Email ID: ")
        iemail = input()
        Account.email = re.findall(r'([a-zA-Z0-9+._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+)', iemail)
        print("Please Enter your Date of Birth: ")
        idob = input("(in dd/mm/yyyy format) ")
        Account.dob = re.findall(r'\d{2}[/]\d{2}[/]\d{4}', idob)
        Account.nationality = input("Please enter your Nationality: ")
        showaccDetails3()
        return 0
    else:
        print("\n✖ Invalid Input. Please try again!!")
        accDetails2()        

def showAccDetails2():
    print("\nYour Account Details: ")
    print("Name          - ", Account.name)    
    print("Age           - ", Account.age)
    print("Sex           - ", Account.sex)
    print("Phone number  - ", Account.phoneno)
    print("Email ID      - ", Account.email)
    print("Date of Birth - ", Account.dob)
    print("Nationality   - ", Account.nationality)
    print("\nDo you want to continue with this account?  ")
    za = input("yes or no: ").lower()
    if za == "yes":
        chooseLanguage()
    elif za == "no":
        accDetails2()
    else:
        print("\nThanks for booking with us :) ")
        print("\nHAVE A NICE DAY AHEAD!!\n")
        exit()     

def showaccDetails3():
    print("\n✔ ACCOUNT CREATED ✔")
    print("\nYour Account Details: ")
    print("Name          - ", Account.name)    
    print("Age           - ", Account.age)
    print("Sex           - ", Account.sex)
    print("Phone number  - ", Account.phoneno)
    print("Email ID      - ", Account.email)
    print("Date of Birth - ", Account.dob)
    print("Nationality   - ", Account.nationality)
    print("\nPress 1 to continue or 2 to exit:  ")
    zk = int(input())
    if zk == 1:
        chooseLanguage()
    elif zk == 2:
        print("\nThank You for creating another account ✔\n")
        print("\nThanks for booking with us :) ")
        print("\nHAVE A NICE DAY AHEAD!!\n")
        print("Hope to see you back soon!\n")
        exit()

def chooseTimings():
    ta1 = {
        "0": "MONDAY",
        "1": "10.00 - 13.00",
        "2": "13.10 - 16.10",
        "3": "16.20 - 19.20",
        "4": "19.30 - 22.30"
    }
    ta2 = {
        "0": "TUESDAY",
        "1": "10.15 - 13.15",
        "2": "13.25 - 16.25",
        "3": "16.35 - 19.35",
        "4": "19.45 - 22.45"
    }
    ta3 = {
        "0": "WEDNESDAY",
        "1": "10.45 - 13.45",
        "2": "13.55 - 16.55",
        "3": "17.05 - 20.05",
        "4": "20.15 - 23.15"
    }
    ta4 = {
        "0": "THURSDAY",
        "1": "10.30 - 13.30",
        "2": "13.40 - 16.40",
        "3": "16.50 - 19.50",
        "4": "20.00 - 22.45"
    }
    ta5 = {
        "0": "FRIDAY",
        "1": "12.00 - 14.45",
        "2": "15.15 - 17.45",
        "3": "18.00 - 20.45",
        "4": "21.00 - 23.45"
    }
    print("\nDays and Timings: ")
    print("\n", ta1, "\n\n", ta2, "\n\n", ta3, "\n\n", ta4, "\n\n", ta5)
    print("\nMonday -----> 1")
    print("Tuesday ----> 2")
    print("Wednesday --> 3")
    print("Thursday ---> 4")
    print("Friday -----> 5")
    print("\nOR Press 6 to go back:")
    print("\nChoose the day of your choice: ")
    tt = int(input(">> "))
    if tt == 1:
        Ticket.price = Ticket.price + 75
        Movie.movieDay = ta1['0']
        print("The Day you've chosen:", Movie.movieDay)
        t = input("Select your time: 1 / 2 / 3 / 4 ~ ")
        Movie.movieTime = ta1[t]
        print("\nYour selected time is: ", Movie.movieTime)
        print("\nDo you want to continue? ")
        ch = int(input("Press 1 to Continue or 2 to go back: "))
        if ch == 1:
            chooseNoOfSeats()
        elif ch == 2:
            chooseTimings()     
    elif tt == 2:
        Movie.movieDay = ta2['0']
        print("The Day you've chosen:", Movie.movieDay)
        t = input("Select your time: 1 / 2 / 3 / 4 ~ ")
        Movie.movieTime = ta2[t]
        print("\nYour selected time is: ", Movie.movieTime)
        print("\nDo you want to continue? ")
        ch = int(input("Press 1 to Continue or 2 to go back: "))
        if ch == 1:
            chooseNoOfSeats()
        elif ch == 2:
            chooseTimings() 
    elif tt == 3:
        Movie.movieDay = ta3['0']
        print("The Day you've chosen:", Movie.movieDay)
        t = input("Select your time: 1 / 2 / 3 / 4 ~ ")
        Movie.movieTime = ta3[t]
        print("\nYour selected time is: ", Movie.movieTime)
        print("\nDo you want to continue? ")
        ch = int(input("Press 1 to Continue or 2 to go back: "))
        if ch == 1:
            chooseNoOfSeats()
        elif ch == 2:
            chooseTimings() 
    elif tt == 4:
        Movie.movieDay = ta4['0']
        print("The Day you've chosen:", Movie.movieDay)
        t = input("Select your time: 1 / 2 / 3 / 4 ~ ")
        Movie.movieTime = ta4[t]
        print("\nYour selected time is: ", Movie.movieTime)
        print("\nDo you want to continue? ")
        ch = int(input("Press 1 to Continue or 2 to go back: "))
        if ch == 1:
            chooseNoOfSeats()
        elif ch == 2:
            chooseTimings() 
    elif tt == 5:
        Ticket.price = Ticket.price + 150
        Movie.movieDay = ta5['0']
        print("The Day you've chosen:", Movie.movieDay)
        t = input("Select your time: 1 / 2 / 3 / 4 ~ ")
        Movie.movieTime = ta5[t] 
        print("\nYour selected time is: ", Movie.movieTime)
        print("\nDo you want to continue? ")
        ch = int(input("Press 1 to Continue or 2 to go back: "))
        if ch == 1:
            chooseNoOfSeats()
        elif ch == 2:
            chooseTimings() 
    elif tt == 6:
        Theater()           
    return 0

def chooseTimings2():
    ta1 = {
        "0": "MONDAY",
        "1": "10.00 - 13.00",
        "2": "13.10 - 16.10",
        "3": "16.20 - 19.20",
        "4": "19.30 - 22.30"
    }
    ta2 = {
        "0": "TUESDAY",
        "1": "10.15 - 13.15",
        "2": "13.25 - 16.25",
        "3": "16.35 - 19.35",
        "4": "19.45 - 22.45"
    }
    ta3 = {
        "0": "WEDNESDAY",
        "1": "10.45 - 13.45",
        "2": "13.55 - 16.55",
        "3": "17.05 - 20.05",
        "4": "20.15 - 23.15"
    }
    ta4 = {
        "0": "THURSDAY",
        "1": "10.30 - 13.30",
        "2": "13.40 - 16.40",
        "3": "16.50 - 19.50",
        "4": "20.00 - 22.45"
    }
    ta5 = {
        "0": "FRIDAY",
        "1": "12.00 - 14.45",
        "2": "15.15 - 17.45",
        "3": "18.00 - 20.45",
        "4": "21.00 - 23.45"
    }
    print("\nDays and Timings: ")
    print("\n", ta1, "\n\n", ta2, "\n\n", ta3, "\n\n", ta4, "\n\n", ta5)
    print("\nMonday -----> 1")
    print("Tuesday ----> 2")
    print("Wednesday --> 3")
    print("Thursday ---> 4")
    print("Friday -----> 5")
    print("\nOR Press 6 to go back:")
    print("\nChoose the day of your choice: ")
    tt = int(input(">> "))
    if tt == 1:
        Ticket.price = Ticket.price + 75
        Movie.movieDay = ta1['0']
        print("The Day you've chosen:", Movie.movieDay)
        t = input("Select your time: 1 / 2 / 3 / 4 ~ ")
        Movie.movieTime = ta1[t]
        print("\nYour selected time is: ", Movie.movieTime)
        print("\nDo you want to continue? ")
        ch = int(input("Press 1 to Continue or 2 to go back: "))
        if ch == 1:
            chooseNoOfSeats()
        elif ch == 2:
            chooseTimings2()     
    elif tt == 2:
        Movie.movieDay = ta2['0']
        print("The Day you've chosen:", Movie.movieDay)
        t = input("Select your time: 1 / 2 / 3 / 4 ~ ")
        Movie.movieTime = ta2[t]
        print("\nYour selected time is: ", Movie.movieTime)
        print("\nDo you want to continue? ")
        ch = int(input("Press 1 to Continue or 2 to go back: "))
        if ch == 1:
            chooseNoOfSeats()
        elif ch == 2:
            chooseTimings2() 
    elif tt == 3:
        Movie.movieDay = ta3['0']
        print("The Day you've chosen:", Movie.movieDay)
        t = input("Select your time: 1 / 2 / 3 / 4 ~ ")
        Movie.movieTime = ta3[t]
        print("\nYour selected time is: ", Movie.movieTime)
        print("\nDo you want to continue? ")
        ch = int(input("Press 1 to Continue or 2 to go back: "))
        if ch == 1:
            chooseNoOfSeats()
        elif ch == 2:
            chooseTimings2() 
    elif tt == 4:
        Movie.movieDay = ta4['0']
        print("The Day you've chosen:", Movie.movieDay)
        t = input("Select your time: 1 / 2 / 3 / 4 ~ ")
        Movie.movieTime = ta4[t]
        print("\nYour selected time is: ", Movie.movieTime)
        print("\nDo you want to continue? ")
        ch = int(input("Press 1 to Continue or 2 to go back: "))
        if ch == 1:
            chooseNoOfSeats()
        elif ch == 2:
            chooseTimings2() 
    elif tt == 5:
        Ticket.price = Ticket.price + 150
        Movie.movieDay = ta5['0']
        print("The Day you've chosen:", Movie.movieDay)
        t = input("Select your time: 1 / 2 / 3 / 4 ~ ")
        Movie.movieTime = ta5[t] 
        print("\nYour selected time is: ", Movie.movieTime)
        print("\nDo you want to continue? ")
        ch = int(input("Press 1 to Continue or 2 to go back: "))
        if ch == 1:
            chooseNoOfSeats()
        elif ch == 2:
            chooseTimings2() 
    elif tt == 6:
        TheaterM()           
    return 0

def chooseTimings3():
    ta1 = {
        "0": "MONDAY",
        "1": "10.00 - 13.00",
        "2": "13.10 - 16.10",
        "3": "16.20 - 19.20",
        "4": "19.30 - 22.30"
    }
    ta2 = {
        "0": "TUESDAY",
        "1": "10.15 - 13.15",
        "2": "13.25 - 16.25",
        "3": "16.35 - 19.35",
        "4": "19.45 - 22.45"
    }
    ta3 = {
        "0": "WEDNESDAY",
        "1": "10.45 - 13.45",
        "2": "13.55 - 16.55",
        "3": "17.05 - 20.05",
        "4": "20.15 - 23.15"
    }
    ta4 = {
        "0": "THURSDAY",
        "1": "10.30 - 13.30",
        "2": "13.40 - 16.40",
        "3": "16.50 - 19.50",
        "4": "20.00 - 22.45"
    }
    ta5 = {
        "0": "FRIDAY",
        "1": "12.00 - 14.45",
        "2": "15.15 - 17.45",
        "3": "18.00 - 20.45",
        "4": "21.00 - 23.45"
    }
    print("\nDays and Timings: ")
    print("\n", ta1, "\n\n", ta2, "\n\n", ta3, "\n\n", ta4, "\n\n", ta5)
    print("\nMonday -----> 1")
    print("Tuesday ----> 2")
    print("Wednesday --> 3")
    print("Thursday ---> 4")
    print("Friday -----> 5")
    print("\nOR Press 6 to go back:")
    print("\nChoose the day of your choice: ")
    tt = int(input(">> "))
    if tt == 1:
        Ticket.price = Ticket.price + 75
        Movie.movieDay = ta1['0']
        print("The Day you've chosen:", Movie.movieDay, "\n")
        t = input("Select your time: 1 / 2 / 3 / 4 ~ ")
        Movie.movieTime = ta1[t]
        print("\nYour selected time is: ", Movie.movieTime)
        print("\nDo you want to continue? ")
        ch = int(input("Press 1 to Continue or 2 to go back: "))
        if ch == 1:
            chooseNoOfSeats()
        elif ch == 2:
            chooseTimings3()     
    elif tt == 2:
        Movie.movieDay = ta2['0']
        print("The Day you've chosen:", Movie.movieDay, "\n")
        t = input("Select your time: 1 / 2 / 3 / 4 ~ ")
        Movie.movieTime = ta2[t]
        print("\nYour selected time is: ", Movie.movieTime)
        print("\nDo you want to continue? ")
        ch = int(input("Press 1 to Continue or 2 to go back: "))
        if ch == 1:
            chooseNoOfSeats()
        elif ch == 2:
            chooseTimings3() 
    elif tt == 3:
        Movie.movieDay = ta3['0']
        print("The Day you've chosen:", Movie.movieDay, "\n")
        t = input("Select your time: 1 / 2 / 3 / 4 ~ ")
        Movie.movieTime = ta3[t]
        print("\nYour selected time is: ", Movie.movieTime)
        print("\nDo you want to continue? ")
        ch = int(input("Press 1 to Continue or 2 to go back: "))
        if ch == 1:
            chooseNoOfSeats()
        elif ch == 2:
            chooseTimings3() 
    elif tt == 4:
        Movie.movieDay = ta4['0']
        print("The Day you've chosen:", Movie.movieDay, "\n")
        t = input("Select your time: 1 / 2 / 3 / 4 ~ ")
        Movie.movieTime = ta4[t]
        print("\nYour selected time is: ", Movie.movieTime)
        print("\nDo you want to continue? ")
        ch = int(input("Press 1 to Continue or 2 to go back: "))
        if ch == 1:
            chooseNoOfSeats()
        elif ch == 2:
            chooseTimings3() 
    elif tt == 5:
        Ticket.price = Ticket.price + 150
        Movie.movieDay = ta5['0']
        print("The Day you've chosen:", Movie.movieDay, "\n")
        t = input("Select your time: 1 / 2 / 3 / 4 ~ ")
        Movie.movieTime = ta5[t] 
        print("\nYour selected time is: ", Movie.movieTime)
        print("\nDo you want to continue? ")
        ch = int(input("Press 1 to Continue or 2 to go back: "))
        if ch == 1:
            chooseNoOfSeats()
        elif ch == 2:
            chooseTimings3() 
    elif tt == 6:
        TheaterX()           
    return 0

def chooseCenter():
    tC = ["INOX", "IMAX 3D", "PVR", "MAXUS", "INOX INSIGNIA"]
    print("\nChoose the Center of your choice:\n")
    print("1 --->", tC[0])
    print("2 --->", tC[1])
    print("3 --->", tC[2])
    print("4 --->", tC[3])
    print("5 --->", tC[4])
    print("\nOR Press 6 to go back:")
    screenC = int(input(">> "))
    if screenC == 1:
        Movie.movieCenter = tC[0]
        print("\nYour selected Center is: ", Movie.movieCenter)
        print("\nDo you want to continue? ")
        ch = int(input("Press 1 to Continue or 2 to go back: "))
        if ch == 1:
            Theater()
        elif ch == 2:
            chooseCenter()
    elif screenC == 2:
        Movie.movieCenter = tC[1]
        print("\nYour selected Center is: ", Movie.movieCenter)
        print("\nDo you want to continue? ")
        ch = int(input("Press 1 to Continue or 2 to go back: "))
        if ch == 1:
            TheaterM()
        elif ch == 2:
            chooseCenter()
    elif screenC == 3:
        Movie.movieCenter = tC[2]
        print("\nYour selected Center is: ", Movie.movieCenter)
        print("\nDo you want to continue? ")
        ch = int(input("Press 1 to Continue or 2 to go back: "))
        if ch == 1:
            Theater()
        elif ch == 2:
            chooseCenter()
    elif screenC == 4:
        Movie.movieCenter = tC[3]
        print("\nYour selected Center is: ", Movie.movieCenter)
        print("\nDo you want to continue? ")
        ch = int(input("Press 1 to Continue or 2 to go back: "))
        if ch == 1:
            Theater()
        elif ch == 2:
            chooseCenter()
    elif screenC == 5:
        Movie.movieCenter = tC[3]
        print("\nYour selected Center is: ", Movie.movieCenter)
        print("\nDo you want to continue? ")
        ch = int(input("Press 1 to Continue or 2 to go back: "))
        if ch == 1:
            TheaterX()
        elif ch == 2:
            chooseCenter()                               
    elif screenC == 6:
        chooseLanguage()
    else:
        print("\n✖ PLEASE ENTER A VALID CHOICE!")
        chooseCenter()          
    return 0    

def movie_E():
    Ticket.price = 0
    mE = ["Top Gun: Maverick", "Thor: Love and Thunder", "Jurassic World: Dominion", "Black Adam", "Elvis"]
    print("\nChoose the movie of your choice:\n")
    print("1 --->", mE[0])
    print("2 --->", mE[1])
    print("3 --->", mE[2])
    print("4 --->", mE[3])
    print("5 --->", mE[4])
    print("\nOR Press 6 to go back:")
    movieE = int(input(">> "))
    if movieE == 1:
        Movie.movieName = mE[0]
        print("\nYour selected movie is: ", Movie.movieName)
        print("\nDo you want to continue? ")
        ch = int(input("Press 1 to Continue or 2 to go back: "))
        if ch == 1:
            chooseCenter()
        elif ch == 2:
            movie_E()
    elif movieE == 2:
        Movie.movieName = mE[1]
        print("\nYour selected movie is: ", Movie.movieName)
        print("\nDo you want to continue? ")
        ch = int(input("Press 1 to Continue or 2 to go back: "))
        if ch == 1:
            chooseCenter()
        elif ch == 2:
            movie_E()
    elif movieE == 3:
        Movie.movieName = mE[2]
        print("\nYour selected movie is: ", Movie.movieName)
        print("\nDo you want to continue? ")
        ch = int(input("Press 1 to Continue or 2 to go back: "))
        if ch == 1:
            chooseCenter()
        elif ch == 2:
            movie_E()
    elif movieE == 4:
        Movie.movieName = mE[3]
        print("\nYour selected movie is: ", Movie.movieName)
        print("\nDo you want to continue? ")
        ch = int(input("Press 1 to Continue or 2 to go back: "))
        if ch == 1:
            chooseCenter()
        elif ch == 2:
            movie_E()
    elif movieE == 5:
        Movie.movieName = mE[4]
        print("\nYour selected movie is: ", Movie.movieName)
        print("\nDo you want to continue? ")
        ch = int(input("Press 1 to Continue or 2 to go back: "))
        if ch == 1:
            chooseCenter()
        elif ch == 2:
            movie_E()   
    elif movieE == 6:
        chooseLanguage()
    else:
        print("\n✖ PLEASE ENTER A VALID CHOICE!")
        movie_E()          
    return 0    

def movie_H():
    Ticket.price = 0
    mH = ["JugJugg Jeeyo", "Bhool Bhulaiyaa 2", "MAJOR", "Janhit Mein Jaari", "Samrat Prithviraj"]
    print("\nChoose the movie of your choice:\n")
    print("1 --->", mH[0])
    print("2 --->", mH[1])
    print("3 --->", mH[2])
    print("4 --->", mH[3])
    print("5 --->", mH[4])
    print("\nOR Press 6 to go back:")
    movieH = int(input(">> "))
    if movieH == 1:
        Movie.movieName = mH[0]
        print("\nYour selected movie is: ", Movie.movieName)
        print("\nDo you want to continue? ")
        ch = int(input("Press 1 to Continue or 2 to go back: "))
        if ch == 1:
            chooseCenter()
        elif ch == 2:
            movie_H()
    elif movieH == 2:
        Movie.movieName = mH[1]
        print("\nYour selected movie is: ", Movie.movieName)
        print("\nDo you want to continue? ")
        ch = int(input("Press 1 to Continue or 2 to go back: "))
        if ch == 1:
            chooseCenter()
        elif ch == 2:
            movie_H()
    elif movieH == 3:
        Movie.movieName = mH[2]
        print("\nYour selected movie is: ", Movie.movieName)
        print("\nDo you want to continue? ")
        ch = int(input("Press 1 to Continue or 2 to go back: "))
        if ch == 1:
            chooseCenter()
        elif ch == 2:
            movie_H()
    elif movieH == 4:
        Movie.movieName = mH[3]
        print("\nYour selected movie is: ", Movie.movieName)
        print("\nDo you want to continue? ")
        ch = int(input("Press 1 to Continue or 2 to go back: "))
        if ch == 1:
            chooseCenter()
        elif ch == 2:
            movie_H()
    elif movieH == 5:
        Movie.movieName = mH[4]
        print("\nYour selected movie is: ", Movie.movieName)
        print("\nDo you want to continue? ")
        ch = int(input("Press 1 to Continue or 2 to go back: "))
        if ch == 1:
            chooseCenter()
        elif ch == 2:
            movie_H()   
    elif movieH == 6:
        chooseLanguage()
    else:
        print("\n✖ PLEASE ENTER A VALID CHOICE!")
        movie_H()          
    return 0    

def movie_T():
    Ticket.price = 0
    mT = ["Vikram", "Maari", "Asuran", "Enthiran", "DON"]
    print("\nChoose the movie of your choice:\n")
    print("1 --->", mT[0])
    print("2 --->", mT[1])
    print("3 --->", mT[2])
    print("4 --->", mT[3])
    print("5 --->", mT[4])
    print("\nOR Press 6 to go back:")
    movieT = int(input(">> "))
    if movieT == 1:
        Movie.movieName = mT[0]
        print("\nYour selected movie is: ", Movie.movieName)
        print("\nDo you want to continue? ")
        ch = int(input("Press 1 to Continue or 2 to go back: "))
        if ch == 1:
            chooseCenter()
        elif ch == 2:
            movie_T()
    elif movieT == 2:
        Movie.movieName = mT[1]
        print("\nYour selected movie is: ", Movie.movieName)
        print("\nDo you want to continue? ")
        ch = int(input("Press 1 to Continue or 2 to go back: "))
        if ch == 1:
            chooseCenter()
        elif ch == 2:
            movie_T()
    elif movieT == 3:
        Movie.movieName = mT[2]
        print("\nYour selected movie is: ", Movie.movieName)
        print("\nDo you want to continue? ")
        ch = int(input("Press 1 to Continue or 2 to go back: "))
        if ch == 1:
            chooseCenter()
        elif ch == 2:
            movie_T()
    elif movieT == 4:
        Movie.movieName = mT[3]
        print("\nYour selected movie is: ", Movie.movieName)
        print("\nDo you want to continue? ")
        ch = int(input("Press 1 to Continue or 2 to go back: "))
        if ch == 1:
            chooseCenter()
        elif ch == 2:
            movie_T()
    elif movieT == 5:
        Movie.movieName = mT[4]
        print("\nYour selected movie is: ", Movie.movieName)
        print("\nDo you want to continue? ")
        ch = int(input("Press 1 to Continue or 2 to go back: "))
        if ch == 1:
            chooseCenter()
        elif ch == 2:
            movie_T()   
    elif movieT == 6:
        chooseLanguage()
    else:
        print("\n✖ PLEASE ENTER A VALID CHOICE!")
        movie_T()          
    return 0    

def movie_P():
    Ticket.price = 0
    mP = ["Carry on jatta", "Chal Mera Putt", "Jatt and Juliet", "Santa Banta pvt ltd ", "Punjab 1984"]
    print("\nChoose the movie of your choice:\n")
    print("1 --->", mP[0])
    print("2 --->", mP[1])
    print("3 --->", mP[2])
    print("4 --->", mP[3])
    print("5 --->", mP[4])
    print("\nOR Press 6 to go back:")
    movieP = int(input(">> "))
    if movieP == 1:
        Movie.movieName = mP[0]
        print("\nYour selected movie is: ", Movie.movieName)
        print("\nDo you want to continue? ")
        ch = int(input("Press 1 to Continue or 2 to go back: "))
        if ch == 1:
            chooseCenter()
        elif ch == 2:
            movie_P()
    elif movieP == 2:
        Movie.movieName = mP[1]
        print("\nYour selected movie is: ", Movie.movieName)
        print("\nDo you want to continue? ")
        ch = int(input("Press 1 to Continue or 2 to go back: "))
        if ch == 1:
            chooseCenter()
        elif ch == 2:
            movie_P()
    elif movieP == 3:
        Movie.movieName = mP[2]
        print("\nYour selected movie is: ", Movie.movieName)
        print("\nDo you want to continue? ")
        ch = int(input("Press 1 to Continue or 2 to go back: "))
        if ch == 1:
            chooseCenter()
        elif ch == 2:
            movie_P()
    elif movieP == 4:
        Movie.movieName = mP[3]
        print("\nYour selected movie is: ", Movie.movieName)
        print("\nDo you want to continue? ")
        ch = int(input("Press 1 to Continue or 2 to go back: "))
        if ch == 1:
            chooseCenter()
        elif ch == 2:
            movie_P()
    elif movieP == 5:
        Movie.movieName = mP[4]
        print("\nYour selected movie is: ", Movie.movieName)
        print("\nDo you want to continue? ")
        ch = int(input("Press 1 to Continue or 2 to go back: "))
        if ch == 1:
            chooseCenter()
        elif ch == 2:
            movie_P()   
    elif movieP == 6:
        chooseLanguage()
    else:
        print("\n✖ PLEASE ENTER A VALID CHOICE!")
        movie_P()          
    return 0    

def movie_M():
    Ticket.price = 0
    mM = ["Dharamaveer", "Sairat", "Bhirkit", "Sarsenapati Hambirrao", "Medium Spicy"]
    print("\nChoose the movie of your choice:\n")
    print("1 --->", mM[0])
    print("2 --->", mM[1])
    print("3 --->", mM[2])
    print("4 --->", mM[3])
    print("5 --->", mM[4])
    print("\nOR Press 6 to go back:")
    movieM = int(input(">> "))
    if movieM == 1:
        Movie.movieName = mM[0]
        print("\nYour selected movie is: ", Movie.movieName)
        print("\nDo you want to continue? ")
        ch = int(input("Press 1 to Continue or 2 to go back: "))
        if ch == 1:
            chooseCenter()
        elif ch == 2:
            movie_M()
    elif movieM == 2:
        Movie.movieName = mM[1]
        print("\nYour selected movie is: ", Movie.movieName)
        print("\nDo you want to continue? ")
        ch = int(input("Press 1 to Continue or 2 to go back: "))
        if ch == 1:
            chooseCenter()
        elif ch == 2:
            movie_M()
    elif movieM == 3:
        Movie.movieName = mM[2]
        print("\nYour selected movie is: ", Movie.movieName)
        print("\nDo you want to continue? ")
        ch = int(input("Press 1 to Continue or 2 to go back: "))
        if ch == 1:
            chooseCenter()
        elif ch == 2:
            movie_M()
    elif movieM == 4:
        Movie.movieName = mM[3]
        print("\nYour selected movie is: ", Movie.movieName)
        print("\nDo you want to continue? ")
        ch = int(input("Press 1 to Continue or 2 to go back: "))
        if ch == 1:
            chooseCenter()
        elif ch == 2:
            movie_M()
    elif movieM == 5:
        Movie.movieName = mM[4]
        print("\nYour selected movie is: ", Movie.movieName)
        print("\nDo you want to continue? ")
        ch = int(input("Press 1 to Continue or 2 to go back: "))
        if ch == 1:
            chooseCenter()
        elif ch == 2:
            movie_M()   
    elif movieM == 6:
        chooseLanguage()
    else:
        print("\n✖ PLEASE ENTER A VALID CHOICE!")
        movie_M()          
    return 0    

def chooseLanguage():    
    print("\nEnglish - 1\nHindi   - 2\nTamil   - 3\nPunjabi - 4\nMarathi - 5\nExit    - 6")
    while True:
        x = int(input("\nChoose the Language of the Movie: "))
        if x == 1:    
            print("\nYour Chosen Language is ENGLISH. Do you want to continue?")
            xe = input("yes or no: ").lower()
            if xe == "yes":
                movie_E() 
            else:
                pass
        elif x == 2:    
            print("\nYour Chosen Language is HINDI. Do you want to continue?")
            xh = input("yes or no: ").lower()
            if xh == "yes":
                movie_H() 
            else:
                pass
        
        elif x == 3:
            print("\nYour Chosen Language is TAMIL. Do you want to continue?")
            xt = input("yes or no: ").lower()
            if xt == "yes":
                movie_T()
            else:
                pass  
        
        elif x == 4:
            print("\nYour Chosen Language is PUNJABI. Do you want to continue?")
            xp = input("yes or no: ").lower()
            if xp == "yes":
                movie_P()
            else:
               pass   
        
        elif x == 5:
            print("\nYour Chosen Language is MARATHI. Do you want to continue?")
            xm = input("yes or no: ").lower()
            if xm == "yes":
               movie_M() 
            else:
                pass 
        
        elif x == 6:
            print("\nHaving trouble in booking?")
            print("You can always call on our toll-free number or write a mail to us regarding the issue.")
            print("Hope to see you back soon!!")
            break
        else:
            print("Please enter a valid choice ✖")

#print("\nThanks for booking with us :) ")
#print("\nHAVE A NICE DAY AHEAD!!\n")        

def showaccDetails():
    print("\n✔ ACCOUNT CREATED ✔")
    print("\nYour Account Details: ")
    print("Name          - ", Account.name)    
    print("Age           - ", Account.age)
    print("Sex           - ", Account.sex)
    print("Phone number  - ", Account.phoneno)
    print("Email ID      - ", Account.email)
    print("Date of Birth - ", Account.dob)
    print("Nationality   - ", Account.nationality)
    print("\nPress 1 to continue or 2 to exit:  ")
    xcd = int(input())
    if xcd == 1:
        chooseLanguage()
    elif xcd == 2:
        print("\nThanks for creating an account ✔")
        print("Hope to see you back soon!\n")
        exit()

def accDetails():
    Account.name = input("\nPlease Enter your Name >> ")
    Account.age = int(input("Please Enter your Age >> "))
    g = input("Please Enter your Sex (M/F/O) >> ").upper()
    if g == "M":
        Account.sex = g
        Account.phoneno = int(input("Please Enter your Phone number >> "))
        print("Please Enter your Email ID: ")
        iemail = input()
        Account.email = re.findall(r'([a-zA-Z0-9+._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+)', iemail)
        print("Please Enter your Date of Birth: ")
        idob = input("(in dd/mm/yyyy format) ")
        Account.dob = re.findall(r'\d{2}[/]\d{2}[/]\d{4}', idob)
        Account.nationality = input("Please enter your Nationality: ")
        showaccDetails()
        return 0
    elif g == "F":
        Account.sex = g
        Account.phoneno = int(input("Please Enter your Phone number >> "))
        print("Please Enter your Email ID: ")
        iemail = input()
        Account.email = re.findall(r'([a-zA-Z0-9+._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+)', iemail)
        print("Please Enter your Date of Birth: ")
        idob = input("(in dd/mm/yyyy format) ")
        Account.dob = re.findall(r'\d{2}[/]\d{2}[/]\d{4}', idob)
        Account.nationality = input("Please enter your Nationality: ")
        showaccDetails()
        return 0
    elif g == "O":
        Account.sex = g
        Account.phoneno = int(input("Please Enter your Phone number >> "))
        print("Please Enter your Email ID: ")
        iemail = input()
        Account.email = re.findall(r'([a-zA-Z0-9+._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+)', iemail)
        print("Please Enter your Date of Birth: ")
        idob = input("(in dd/mm/yyyy format) ")
        Account.dob = re.findall(r'\d{2}[/]\d{2}[/]\d{4}', idob)
        Account.nationality = input("Please enter your Nationality: ")
        showaccDetails()
        return 0
    else:
        print("\n✖ Invalid Input. Please try again!!")
        accDetails()    

def createAccountPrompt():
    print("\nPress 1 to Create a New Account: ")
    print("OR")
    print("Press 2 to exit\n")
    xcc = int(input(">> "))
    while(1):
        if xcc == 1:
            accDetails()
        elif xcc == 2:
            exit()

if __name__ == '__main__':
    print("\nWELCOME TO MOVIE TICKET BOOKING SYSTEM: ")
    createAccountPrompt()
    #chooseLanguage()
