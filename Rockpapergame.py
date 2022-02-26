import random
def play():
    user = input("'s' for scissors,'p'for paper,'r'for rock\n")
    computer = random.choice(['r','s','p'])
    
    if user == computer:
        return "Its a tie"
    
    if win(user, computer):
        return 'You Won!'
    return "You Lost!"
    
#r > s, s > p, p > r

def win(player,opponent):
    if (player =='r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True
    
print(play())