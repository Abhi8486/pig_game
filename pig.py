import random 
# roll function which return random value from 2 to 4
def roll(): 
    return random.randint(1,6)

def score_reach(players):
    max_point =20
    val =list(players.values())
    for i in val:
        if(i >= max_point):
            return True
        
def display(players):
    print(f"--------------------------------------")
    for i in players:
        print(f"Total score of {i} is {players[i]}")
    print(f"--------------------------------------")

# here we get no of players playing game
no_of_players = int(input('Enter number of players (2-4)'))
if not(no_of_players <2 or no_of_players >4):
    print('please enter number of players between 2 to 4:')

# we will make a dictionary which store player name as key and its score as value 
players ={}
for i in range(no_of_players):
    name = input("enter player name:")
    players[name]=0
max_point =20
# we will make a loop which will run until one player reach max_point
flag=0
while True:
    if flag == 1:
        break
    else:
        for i in (players):
            if flag == 1:
                break
            display(players)
            current_score = 0
            while True:
                if score_reach(players) == True:
                    flag = 1
                    print("game over someone reached 20 points!")
                    break
                print(f"{i}'s turn")
                print(f"Current score : {current_score}" )
                roll_hold = input("Enter yes to roll dice or Enter no to hold score:")
                if roll_hold.lower() == 'no':
                    temp = players[i]
                    temp += current_score
                    players.update({i:temp})
                    print(f" total scoreof player {i} : {players[i]}" )
                    break
                elif roll_hold.lower() == 'yes':
                    roll_dice = roll()
                    print("you rolled a", roll_dice)
                    if roll_dice ==1:
                        break
                    else:
                        current_score += roll_dice
