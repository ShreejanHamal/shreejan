height = int(input("enter your height: "))
if height >= 3:
    print("you can ride ")
    age =int(input("enter your age: "))
    if age < 8:
        print("ride is free")
    else:
        print("you have to pay RS.600")
else:
    print("sorry you cannot go on a ride")