import numpy as np
import time as t
brd = np.zeros((3, 3)).astype(int)

def check_win():
    if any(np.sum(brd, 1)==3) or any(np.sum(brd, 0)==3) or sum(np.diag(brd[::-1]))==3 or sum(np.diag(brd))==3:
        return True
    if any(np.sum(brd, 1)==-3) or any(np.sum(brd, 0)==-3) or sum(np.diag(brd[::-1]))==-3 or sum(np.diag(brd))==-3:
        return True
    return False

def play_turn():
    x = int(input(f"What is player {turn}\'s x position? : "))
    y = int(input(f"What is player {turn}\'s y position? : "))
    try:
        if brd[y, x]==0:
            brd[y, x]=turn
        else:
            play_turn()
    except IndexError:
        play_turn()

turn = 1
move = 9
print("\n======TIC TAC TOE=======\n".center(20))
print("======RULES=======\n".center(20))
t.sleep(2)
print("Players are named 1 and -1".center(20))
print("X axis is from left to right [positions spanning from 0 to 2]")
print("Y axis is from top to bottom [positions spanning from 0 to 2]\n")
print("Let's play!")
while move>0:
    print(brd)
    play_turn()
    if check_win():
        print(f"Player {turn} has won!")
        break
    turn = turn*-1
    move = move-1

