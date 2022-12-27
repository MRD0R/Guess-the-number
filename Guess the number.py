import random as r
from math import *

def is_valid(a):
    if 1<=a and a<=100:
        return True
    return False

t = 'yes'
while t == 'yes':
    y, cnt = r.randint(1,100), 0
    print(y, "Welcome, let's play!", sep = '\n')
    while True:
        x = int(input())
        if is_valid(x):
            if x == y:
                print('GG WP!')
                cnt += 1
                break
            elif x>y:
                print('Try again. Your number is more than conceived!')
                cnt += 1
            else :
                print('Try again. Your number is less than conceived!')
                cnt += 1 
        else:   
            print('Maybe you will try to put a number in interval from 1 to 100?')
            cnt += 1
    if cnt == 1:
        print('Thanks for the game. You count of moves is 1!!!')
    else :
        print('Thanks for the game. Your count of moves is', cnt, '!!!')
    t = input('Do you wanna play again? (yes or no)')