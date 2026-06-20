# 1. დაწერეთ პროგრამა, რომელიც მომხმარებელს შეეკითხება მართკუთხა სამკუთხედის კათეტების სიგრძეს(მთელი დადებითი რიცხვი) და გამოითვლის 
# ამ სამკუთხედის ჰიპოთენუზის სიგრძეს და ფართობს.

leg1 = int(input("Enter the length of the first leg: "))
leg2 = int(input("Enter the length of the second leg: "))

hypotenuse = (leg1**2 + leg2**2)**0.5
area = 0.5 * leg1 * leg2

print(f"The length of the hypotenuse is: {hypotenuse}")
print(f"The area of the triangle is: {area}")

# 2. დაწერეთ პროგრამა, რომელიც მომხმარებელს შეეკითხება წამების რაოდენობას და გამოიტანეთ საათების, წუთების და წამების
# რაოდენობა (მაგ. 20000 წამი არის  5 საათი, 33 წუთი, 20 წამი)

total_seconds = int(input("Enter the total number of seconds: "))

hours = total_seconds // 3600
minutes = (total_seconds % 3600) // 60
seconds = total_seconds % 60

print(f"{hours} hours, {minutes} minutes, {seconds} seconds")