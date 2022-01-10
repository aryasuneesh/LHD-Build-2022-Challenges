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
        i.strip('\'').strip("\'")
        return i
    elif i[0]=="\'" or i[-1]=="\'":
        i.strip('\'')
        return i
    elif i[0]=="\"" or i[-1]=="\"":
        i.strip('\"')
        return i

p = 'y'
while p=='y' or p=='Y':
    print(" ======ArticleAnalyser======")
    print()
    artclTitle = input("    Enter article title:")
    artclList = artclTitle.split(" ")
    posCount, negCount = 0, 0
    for i in artclList:
        k = apostrophecheck(i)
        for j in poslist:
            if k==j[0]:
                posCount+=1

    for i in artclList:
        k = apostrophecheck(i)
        for j in neglist:
            if k==j[0]:
                negCount+=1

    if posCount>negCount:
        print(" The article is POSITIVE")
        p = input(" Would you like to check another article? (y/n): ")
    elif posCount==negCount:
        print(" The article is NEUTRAL")
        p = input(" Would you like to check another article? (y/n): ")
    elif posCount==0 or negCount==0:
        print(" Unable to compute sentiment")
        p = input(" Would you like to check another article? (y/n): ")
    else:
        print(" The article is NEGATIVE")
        p = input(" Would you like to check another article? (y/n): ")


