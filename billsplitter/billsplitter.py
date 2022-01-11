print("========BILL SPLITTER========")

amt = int(input("Enter amount of bill: "))
frnds = int(input("Enter number of people paying the bill: "))
tips = int(input("What % tip would you like to give?: "))

split = round(float(((tips / 100 +1)*amt)/frnds), 2)
print("Amount to be paid per person: ", split)
