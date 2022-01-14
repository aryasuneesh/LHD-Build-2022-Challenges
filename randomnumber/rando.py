import os
size = 1
rand = os.urandom(size)

def bytes_to_int(rand):
    res = 0
    for b in rand:
        res = res * 256 + int(b)
    print(res)

print("\n=========Random Number Generator ===========\n")

bytes_to_int(rand)