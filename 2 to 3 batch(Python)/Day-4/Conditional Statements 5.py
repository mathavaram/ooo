L = int(input("Enter no. of late return days : "))
if L <= 5:
    F = 0.5
elif L > 5 and L <= 10:
    F = 1
elif L > 10 and L <= 30:
    F = 5
elif L > 30:
    F = None

if F != None:
    print("Your late return fee is ", F)
else:
    print("Your Membership is cancelled")
