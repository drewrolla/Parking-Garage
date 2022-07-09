# attributes needed: 
# tickets --> list []
# parkingSpaces --> list []
# currentTicket --> dictionary {}

class Parking():
    tickets = [range(50)]
    parkingSpaces = [range(50)]

    def __init__(self, parkingDict):
        parkingDict = {1 : ['available', 'unpaid'],
        2 : ['available', 'unpaid'],
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
        self.parkingDict = parking.Dict

    def takeTicket(self): # decrease tickets -1/ decrease spaces -1 | will use a list
        takenSpots = []
        for spot in self.parkingDict:
            if self.parkingDict[spot][0] == 'available':
                print(f"Your parking spot is {spot}")
            takenSpots.append(self.parkingDict[spot])
            while True:
                if self.parkingDict[spot][1] == 'unpaid':
                    tickets -= 1
                    parkingSpaces -= 1
            break
        
    def payForParking(self): # will use the dictionary = {1 : ['available , 'not paid']}
        
        while True:
            askUser = input("Did you pay? Yes / No").lower()
            for spot in self.parkingDict:
                if askUser == 'yes':
                    self.parkingDict[spot][1] = 'paid'
                    print('Thanks for coming. Your parking pass expires in 15 minutes.')
                    break
                elif askUser == 'no':
                    print("Please pay for parking before leaving.")
                    break
                else:
                    print("Invalid input. Please type yes or no.")

    def leaveGarage(self): # will use both lists
        while True:
            askUser1 = input("Have you paid for your ticket? Yes / no.").lower()
            for spot in self.parkingDict:
                if askUser1 == 'yes':
                    print("thank you, have a nice day!")
                    while True:
                        if self.parkingDict[spot][1] == 'paid':
                            tickets += 1
                            parkingSpaces += 1
                        break
                    elif askUser1 == 'no':
                        print("please pay for your ticket now.")
                    else:
                        print('Invalid input. Please Try again.')

def run():
    game = Parking()
    while True:
        prompt = input("What do you want to do? Park / Pay / Leave : ").lower()
        if prompt == 'park':
            game.taketicket()
        elif prompt =='pay':
            game.payforParking()
        elif prompt == 'leave':
            game.leaveGarage()
        else:
            print('Inalid. Please try again.')

run()
