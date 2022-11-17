H = int(input("Hardness of the steel = "))
C = float(input("Carbon content of the steel = "))
T = int(input("Tensile strength of the steel = "))
"""global Cond1
global Cond2
global Cond3"""
if H > 50:
    Cond1 = True
else:
    Cond1 = False
if C < 0.7:
    Cond2 = True
else:
    Cond2 = False
if T > 5600:
    Cond3 = True
else:
    Cond3 = False
if Cond1 == True and Cond2 == True and Cond3 == True:
    print("The Grade of the steel is '10'")
elif Cond1 == True and Cond2 == True and Cond3 == False:
    print("The Grade of the steel is '9'")
elif Cond1 == False and Cond2 == True and Cond3 == True:
    print("The Grade of the steel is '8'")
elif Cond1 == True and Cond2 == False and Cond3 == True:
    print("The Grade of the steel is '7'")
elif Cond1 == True or Cond2 == True or Cond3 == True:
    print("The Grade of the steel is '6'")
elif Cond1 == False and Cond2 == False and Cond3 == False:
    print("The Grade of the steel is '5'")




