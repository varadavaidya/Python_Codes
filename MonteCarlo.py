import random
def rolldice():
    roll=random.randint(1,100)
    if roll==100:
        #print(roll,"roll was 100,you lose.Play Again ")
        return False
    elif roll<=50:
        #print(roll,"roll was 1-50,you lose.Play again")
        return False
    elif 100>roll>50:
        #print(roll,"roll was 51-99, you won")
        return True
    return roll


def simple_bettor(funds,initial_wager,wager_count):
    value=funds
    wager=initial_wager
    current_wager=0
    while current_wager<wager_count:
        if rolldice():
            value+=wager
        else:
            value-=wager

        current_wager+=1

    if value<0:
        value='broke'
    print("funds:",value)


x=0
while x<100: #hundred betters
    simple_bettor(10000, 100, 10000)  # the more we run this line, we will get different set of values
    x+=1





