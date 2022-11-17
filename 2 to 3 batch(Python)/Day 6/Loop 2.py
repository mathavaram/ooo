

#for N in range(3):
N = list(input("ENTER 3 NUMBERs : "))
if ((list[0] > list[1]) and (list[0] > list[2])):
    d = list[0]
elif (list[1] > list[2]):
     d = list[1]
else:
    d = list[2]

    print("The greatest number is ", d)

"""a = int(input("ENTER A NUMBER : "))
b = int(input("ENTER A NUMBER : "))
c = int(input("ENTER A NUMBER : "))
if ((a>b) and (a>c)):
    d = a
elif (b>c):
    d = b
else:
    d = c

print("The greatest number is ", d)"""
