import mpmath as mp

print("\n=======================PI=======================\n")
mp.mp.dps = int(input("Enter number of digits of pi to display: "))
print("Pi: ", mp.mp.pi, "\n")