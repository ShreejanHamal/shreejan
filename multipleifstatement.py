name = input("enter your full name: ")
height = float(input("enter your height: "))
bill = 0
if height >=3:
    print(f"hello {name} you can take a ride")
    age = int(input("enter your age: "))
    if age <12:
        bill = 150
        print("the ride will cost RS.150")
    elif age <= 18:
        bill = 250
        print("the ride will cost you RS. 250")
    else:
        bill = 500
        print("the ride will cost you RS.500")
    want_photo=input("do you want to take a photo(Y/N)?")
    if want_photo== 'y' or want_photo== 'Y':
        bill = bill+50
        print(f"your total bill is {bill}")
    if want_photo=='n' or 'N':
        bill= bill
        print(f"your total bill is {bill}")  
else:
    print(f"hello {name}. unfortunately you cannot take this ride")   
    



