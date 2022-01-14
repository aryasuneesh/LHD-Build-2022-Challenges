print("\n===========SORT LIST=============\n")
print("")
def bubbleSort(list):
    n = len(list)
    for i in range(n):
        for j in range(0, n-i-1):
            if list[j] > list[j+1] :
                list[j], list[j+1] = list[j+1], list[j]
    return list

list = eval(input("Enter list of number, enclosed in square brackets: "))
l2 = bubbleSort(list)
print("Sorted list: ", l2, "\n")