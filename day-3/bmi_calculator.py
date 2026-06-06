print("Welcome to the BMI Calculator with Interpretations!")
height_of_person = float(input("Enter your height in cm: "))
weight_of_person = float(input("Enter your weight in kg: "))
bmi = weight_of_person / ((height_of_person / 100) ** 2)
print(f"Your BMI is {round(bmi, 2)}.")
if bmi < 18.5:
    print("You are underweight.")
elif 18.5 <= bmi < 25:
    print("You have a normal weight.")
elif 25 <= bmi < 30:
    print("You are slightly overweight.")
elif 30 <= bmi < 35:
    print("You are obese.")
else:
    print("You are clinically obese.")
