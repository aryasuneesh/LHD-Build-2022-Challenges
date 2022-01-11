import random

print("     =====ROCK PAPER SCISSORS======")
print()
print(" [1]rock ==== [2]paper ==== [3]scissors")
print()

p='y'

while p=='y' or p=="Y":
    i = random.randrange(0, 2)
    rps = ["rock", "paper", "scissors"] 
    ui = int(input("     Enter your choice: "))
    u = ui-1

    print("     your choice : {}, bot\'s choice: {}".format(rps[u], rps[i] ))
    print()

    if u==i:
        print("     Result = Draw!")
    elif rps[u] == "rock":
        if rps[i] == "scissors":
            print("     Result = You won!")
        elif rps[i]=="paper":
            print("     Result = Bot won!")
    elif rps[u] == "paper":
        if rps[i] == "rock":
            print("     Result = You won!")
        elif rps[i]=="scissors":
            print("     Result = Bot won!")
    elif rps[u] == "scissors":
        if rps[i] == "paper":
            print("     Result = You won!")
        elif rps[i]=="rock":
            print("     Result = Bot won!")
    p = input("     Would you like to play again? (y/n): ")