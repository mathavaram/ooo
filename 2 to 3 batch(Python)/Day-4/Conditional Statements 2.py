Age = int(input("PLEASE ENTER YOUR AGE : "))
Gender = input("PLEASE ENTER YOUR GENDER(M/F) : ")
Gender = Gender[0].lower()
if Age >= 18:
    if Gender == "m":
        print("YOUR ROOM NO IS 5")
    elif Gender == "f":
        print("YOUR ROOM NO IS 6")
else:
    print("YOU ARE NOT ELIGIBLE")
