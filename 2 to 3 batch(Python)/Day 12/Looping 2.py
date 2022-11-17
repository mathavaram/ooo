for x in range(5):
    A = int(input("ENTER A NUMBER : "))
    B = int(input("ENTER A NUMBER : "))
    C = A+B
    print("SUM OF THE TWO NUMBERS IS : ", C)
    for i in range(10):
        t = input("DO YOU WANT TO ADD ANOTHER SET OF NUMBERS? Y / N : ", )
        if t != "Y" and t !="N":
            print("PRINT ONLY 'Y' OR 'N'")
        else:
            break
    if t == "Y":
        continue
    elif t == "N":
        break
    else:
        print("PRINT ONLY 'Y' OR 'N'")
