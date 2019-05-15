# hand and foot scoring tool
import time

print("Time to play - what is the name of the first team?")
team1 = input()
while not team1:
    print("hmm... missing the first team's name, what is it?")
    team1 = input()
print(team1 + ": your team has been created")
print("What is the name of the second team?")
team2 = input()
while not team2:
    print("hmm... missing the second team's name, what is it?")
    team2 = input()
print(team2 + ": your team has been created")
print("Time to play - 4 decks of cards should be shuffled together")
time.sleep(1)

def calc_books(team):
        print(team + ": Let's tally your books-")
        print(team + ": How many wild books do you have (worth 1,000 points each)")
        wild = int(input()) * 1000
        print(team + ": How many books of 7 do you have (worth 750 points each)")
        seven = int(input()) * 750
        print(team + ": How many clean books do you have (worth 500 points each)")
        clean = int(input()) * 500
        print(team + ": How many dirty books do you have (worth 250 points each)")
        dirty = int(input()) * 250
        book = wild + seven + clean + dirty
        return book

def calc_cards(team):
        print(team + ": Let's tally your card points-")
        print(team + ": Player 1 - how many points do you have")
        player_one_points = int(input())
        print(team + ": Player 2 - how many points do you have")
        player_two_points = int(input())
        cards = player_one_points + player_two_points
        return cards        

def card_pickup():
    print("Try to pick up 26 cards.\nPerfectly picking up 26 cards equals 1,000 points")
    time.sleep(3)
    print(team1 + ": How many of you picked up exactly 26 cards? (0, 1, or 2)")
    pickup1 = int(input()) * 1000
    if pickup1 in [1000, 2000]:
        print("Nice! that is %i points" %(pickup1))
    else:
        pickup1 = 0
        print("Better luck next time")
    print(team2 + ": How many of you picked up exactly 26 cards? (0, 1, or 2)")
    pickup2 = int(input()) * 1000
    if pickup2 in [1000, 2000]:
        print("Nice! that is %i points" %(pickup2))
    else:
        pickup2 = 0
        print("Better luck next time")
    print("Play!")
    return pickup1, pickup2

outs = [50, 90, 120 ,150]
t1 = 0
t2 = 0
for i in range(4):
    print("Round %i - %i points to go out" %((i+1), outs[i]))
    pb1, pb2 = card_pickup()
    b1 = calc_books(team1)
    b2= calc_books(team2)
    c1 = calc_cards(team1)
    c2= calc_cards(team2)
    r1 = b1 + c1 + pb1
    r2= b2 + c2 + pb2
    t1 += r1
    t2 += r2
    print('\n' + "%s - Round Points: %i Total Points: %i" %(team1, r1, t1))
    print('\n' + "%s - Round Points: %i Total Points: %i" %(team2, r2, t2) + '\n')
    

print("Game is now done")
print("%s has %i points" %(team1, t1))
print("%s has %i points" %(team2, t2))
if t1 > t2:
    print(team1 + " you win!")
if t1 < t2:
    print(team2 + " you win!")
