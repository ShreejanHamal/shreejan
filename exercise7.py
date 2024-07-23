# order a pizza with addons
size_of_pizza=input("which pizza do you want(Large/Medium/Small)")
bill = 0
if size_of_pizza == 'large' or size_of_pizza=='L' or size_of_pizza=='l':
    bill +=1000
elif size_of_pizza=='medium' or size_of_pizza=='m' or size_of_pizza=='M':
    bill +=750
elif size_of_pizza=='small' or size_of_pizza=='s' or size_of_pizza=='S':    
    bill +=500
else:
    print("choose from different dish in menu.")


add_pepperoni=input("do you want to add pepporoni(Y/N)")
if add_pepperoni=='y' or add_pepperoni=='y':
    if size_of_pizza == 'large' or size_of_pizza=='L' or size_of_pizza=='l':
        bill = bill + 100
    elif size_of_pizza=='medium' or size_of_pizza=='m' or size_of_pizza=='M':
        bill = bill+75
    else:
        bill +=50


extra_cheese=input("do you want to add extra cheese(Y/N)")       
if extra_cheese=='Y' or extra_cheese=='y':
    if size_of_pizza == 'large' or size_of_pizza=='L' or size_of_pizza=='l':
        bill =bill+50
    elif size_of_pizza=='medium' or size_of_pizza=='m' or size_of_pizza=='M':
        bill=bill+40
    else:
        bill =bill+30
print(f"your total bill is {bill}")
