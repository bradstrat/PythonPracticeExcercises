import random #random.randint(x,y)

# objects?

def givecard(*args):
     while True:
     #while int(args)  != 0:
          possiblecards =["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
          randindex = random.randint(0,12)
          randcard = possiblecards[randindex]
          
          return randcard
          #args = int(args) - 1
          print(*args)
               

def blacjack():
     name = input("Welcome! what's your name: ")
     dealer = []
     user = []
     
     dealer.append(givecard(2))
     user.append(givecard(2))
          
     #print("Current cards: {}".format())

     
     #user starts with 2 cards
     

     #there is dealer

     ## Repeats untill stay or bust
          #user chooses to play or stand

          #dealer deals cards

     # if count is 21 win and others lose, if count is over 21 lose,
     # remaining players that are not equal to lose, highest wins
     #notes: if 2 people get 21 dealer wins,

givecard(2)
givecard()

