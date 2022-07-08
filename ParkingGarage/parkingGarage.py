# attributes needed: 
# tickets --> list []
# parkingSpaces --> list []
# currentTicket --> dictionary {}

class Parking():
    

    def __init__(self, parkingDict={}, tickets=[], parkingSpaces=[]):
        parkingDict = {1 : ['available', 'unpaid'],
        2: ['available', 'unpaid'],
        3 : ['available', 'unpaid'],
        4 : ['available', 'unpaid'],
        5 : ['available', 'unpaid'],
        6 : ['available', 'unpaid'],
        7 : ['available', 'unpaid'],
        8 : ['available', 'unpaid'],
        9 : ['available', 'unpaid'],
        10 : ['available', 'unpaid'],
        11 : ['available', 'unpaid'],
        12 : ['available', 'unpaid'],
        13 : ['available', 'unpaid'],
        14 : ['available', 'unpaid'],
        15 : ['available', 'unpaid']
        }
        tickets = 15
        parkingSpaces = 15
        self.parkingDict = parkingDict
        self.tickets = tickets
        self.parkingSpaces = parkingSpaces

    def takeTicket(self): # decrease tickets -1/ decrease spaces -1 | will use a list
        takenSpots = []
        for spot in self.parkingDict:
            if self.parkingDict[spot][0] == 'available': # index into list within dictionary. checks to see if spot is available
                print(f"Your parking spot is {spot}") # prints out what parking spot number you have
                takenSpots.append(self.parkingDict[spot])
                while True:
                    if self.parkingDict[spot][1] == 'unpaid':
                        self.tickets -= 1
                        self.parkingSpaces -= 1
                    break
            break


    def payForParking(self): # will use the dictionary spot1 = { 1 : ['available', 'not paid']}
            for spot in self.parkingDict:
                askUser = input("Did you pay for your ticket? Yes/No: ").lower()
                if askUser == 'yes':
                    self.parkingDict[spot][1] = 'paid'
                    print("Thanks for coming. Your parking pass expires in 15 minutes.")
                    break
                elif askUser == 'no':
                    print("Please pay for parking before leaving.")
                else:
                    print("Invalid input.")

    def leaveGarage(self): # will use both lists
            for spot in self.parkingDict:
                askUser1 = input("Have you paid for your ticket? Yes/No: ").lower()
                if askUser1 == 'yes':
                    print("Thank you, have a nice day!")
                    while True:
                        if self.parkingDict[spot][1] == 'paid':
                            self.tickets += 1
                            self.parkingSpaces += 1
                        break
                    break
                elif askUser1 == 'no':
                    print("Please pay for your ticket now.")
                else:
                    print("Invalid input. Please try again.")

def run():
    game = Parking()
    while True:
        prompt = input("What do you want to do? Park/Pay/Leave/End: ").lower()

        if prompt == 'park':
            game.takeTicket()

        elif prompt == 'pay':
            game.payForParking()

        elif prompt == 'leave':
            game.leaveGarage()
            
        elif prompt == 'end':
            break
        
        else:
            print("Invalid input.")

run()
