height= int(input("Enter your height : "))

if height>=3:
    print("you can go on a ride")
    age = int(input("enter your age: "))  
    if age < 3:
        print("ride is free")
    elif age <=10:
        print("ride will cost 100")
    elif age <= 20:
        print("ride will cost 200")
    else:
        print("ride will cost 500")
else:
    print("fuck off!")
print("come back when you reach our height requirements")