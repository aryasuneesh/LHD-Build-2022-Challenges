pos = open("articleanalysis/positive-words.txt","r")
poslist=[]
for l1 in pos:
    poslist.append(l1.split())
neglist=[]
neg = open("articleanalysis/negative-words.txt","r")
for l2 in neg:
    neglist.append(l2.split())

def apostrophecheck(i):
    if i[0]=="'" and i[-1]=="'":
        i = i[1:-1]
    elif i[0]=="'" or i[0]=="\"":
        i = i[1:]
    elif i[-1]=="'" or i[-1]=="\"":
        i = i[:-1]
    
artclTitle = input("Enter article title:")
artclList = artclTitle.split(" ")
posCount, negCount = 0, 0
for i in artclList:

    for j in poslist:
        if i==j[0]:
            posCount+=1

for i in artclList:
    if i[0]=="'" and i[-1]=="'":
        i = i[1:-1]
    for j in neglist:
        if i==j[0]:
            negCount+=1

if posCount>negCount:
    print("The article is POSITIVE")
elif posCount==negCount:
    print("The article is NEUTRAL")
elif posCount==0 or negCount==0:
    print("Unable to compute sentiment")
else:
    print("The article is NEGATIVE")


