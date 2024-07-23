# elif to measure BMI

weight = float(input("enter your Weight in kg: "))
height = float(input("enter your height in m: "))
bmi= weight/(height*0.3048) ** 2

if bmi < 18.5:
    print(f"your bmi is {bmi} and you are underweight.")
elif bmi < 25:
    print(f"your bmi is {bmi} and have noramalweight")
elif bmi < 30:
    print(f"your bmi is {bmi} and you are over weight")
elif bmi < 35:
    print(f"your bmi is {bmi} and you are obese")
else:
    print(f"your bmi is {bmi} and you are clinically obese")

