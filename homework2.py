# 1. დაწერეთ პროგრამა რომელიც მომხმარებელს ჰკითხავს წონას(კგ) და სიმაღლეს(მ), შეყვანილი მონაცემების 
# საფუძველზე გამოითვლის BMI-ს(Body Mass Index). ფორმულა: წონა გაყოფილი სიმაღლის კვადრატზე
# თუ BMI ნაკლებია 19-ზე, გამოიტანეთ ინფო რომ ის არის underweight
# თუ BMI არის 19 და 25 შორის, გამოიტანეთ ინფო რომ ის არის normalweight
# თუ BMI მეტია 25-ზე, გამოიტანეთ ინფო რომ ის არის overweight

weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (m): "))

bmi = weight / (height ** 2)

if bmi < 19:
    print("You are underweight.")
elif 19 <= bmi < 25:
    print("You are of normal weight.")
else:
    print("You are overweight.")



# 2. დაწერეთ კალკულატორის პროგრამა, რომელიც მომხმარებელს შეეკითხება ორ რიცხვს და არითმეტიკულ ოპერატორს,
# შესაბამისი ოპერატორის საფუძველზე გამოითვლის ამ ორი რიცხვის შედეგს.

first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))
operator = input("Enter an operator (+, -, *, /): ")

if operator == "+":
    result = first_number + second_number
elif operator == "-":
    result = first_number - second_number
elif operator == "*":
    result = first_number * second_number
elif operator == "/":
    result = first_number / second_number
else:
    print("Invalid operator.")
    result = None

if result is not None:
    print(f"The result of {first_number} {operator} {second_number} is {result}")



# 3. დაწერეთ პროგრამა, რომელიც მომხმარებელს შეეკითხება 3 რიცხვს, ჯერ შეამოწმეთ ეს რიცხვები არ უდრიდეს ერთმანეთს,
# თუ რომელიმე ორი ერთმანეთს უდრის, დაპრინტეთ რომ შეიყვანოს განსხვავებული რიცხვები. თუ რიცხვები განსხვავებულია, 
# იპოვეთ ყველაზე დიდი რიცხვი. არ გამოიყენოთ max ფუნქცია!

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

if num1 == num2 or num1 == num3 or num2 == num3:
    print("The numbers must be different.")
else:
    if num1 > num2 and num1 > num3:
        largest = num1
    elif num2 > num1 and num2 > num3:
        largest = num2
    else:
        largest = num3
    print(f"The largest number is: {largest}")  
