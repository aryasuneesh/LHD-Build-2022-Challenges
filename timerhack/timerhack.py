import time
from playsound import playsound

def timerhack(t):
    while t:
        mins, sec = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, sec)
        print(timer, end="\r")
        time.sleep(1)
        t-=1
    playsound("timerhack/Ding-sound-three-times.mp3")
    print("Time's up!")

    
p = 'y'
while p=='y' or p=='Y':
    print(" =====Timer=====")
    print()
    print(" 1. Enter time in seconds")
    print(" 2. Enter time in minutes")
    print(" 3. Enter time in hours")
    print()
    c = int(input("Enter option:"))
    if c==1:
        t = int(input("Enter number of seconds:"))
        timerhack(t)
        p = input("Would you like to use the timer again? (y/n): ")
        
    elif c==2:
        t1 = int(input("Enter number of minutes:"))
        t = t1*60
        timerhack(t)
        p = input("Would you like to use the timer again? (y/n): ")
        
    elif c==3:
        t2 = int(input("Enter number of hours:"))
        t = t2*60*60
        timerhack(t)
        p = input("Would you like to use the timer again? (y/n): ")
    else:
        print("Not valid option. Try again!")
        p = input("Would you like to use the timer again? (y/n): ")
