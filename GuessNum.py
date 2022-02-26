#Guess the number 

import random
def guess():
    x=int(input("Enter a Range:"))
    random_num = random.randint(1,x)
    guess = 0
    while guess != random_num:
        guess = int(input(f'guess a number between 1 and {x}:'))
        if guess < random_num:
            print("Sorry,try again,too low.")
        elif guess > random_num:
            print("Sorry,try again,too high.")
    print(f'Congrats, You have guessed the number {random_num} correctly') 

def computer_guess(x):
    low = 1
    high = x
    feedback ='c'
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f'is {guess} too high (H), too low(L) or correct(c)').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback =='l':
            low = guess + 1
    print(f'Congrats, The computer guessed your number, {guess} correctly!')
    
computer_guess(10)
            
                