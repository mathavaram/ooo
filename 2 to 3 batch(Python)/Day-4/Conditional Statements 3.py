BS = float(input("Please enter your basic salary : "))

if BS < 1500:
    HRA = (BS*(10/100))
    DA = (BS*(90/100))
else:
    HRA = 500
    DA = (BS * (98 / 100))

print("Your gross Salary is : ", BS+HRA+DA)
