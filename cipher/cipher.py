import string

print("\n===========CIPHER============\n")

x = input("Enter the input to cipher: ")
o = ''
s = string.ascii_letters
for i in x:
    for j in range(len(s)):
        if i==s[j]:
            if j-5>0 and j+5<26:
                e = 'X'+s[j+5]+s[j-5]
                o+=e
            else:
                e = 'X'+s[j-1]+s[j+1]
                o+=e
    
print("Cipher text: ", o)
