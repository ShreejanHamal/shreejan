# write a program if the year is leap year or nah

year=int(input("enter the year you wat to check: "))
if year%4==0:
    if year%10==0:
        if year % 400 ==0:
            print("this is a leap year")
        else:
            print("this is not a leap year")
    else:
        print("this is a leap year")
else:
    print("the year is not a leap year")
