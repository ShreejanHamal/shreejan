# WAP to select a random name from a list of names and the person selected will have to pick up the bills
import random
name= input("enter everybody,s naem seprated my comma")
names_lsit=name.split(",")
len = len(names_lsit)
random_choice = random.randint(0,len-1)
print(names_lsit[random_choice])