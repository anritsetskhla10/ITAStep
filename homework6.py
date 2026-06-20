# 1. დაწერეთ პროგრამა, რომელიც შექმნის დიქტს, რომელშიც key-ები იქნება 1-დან 10-ის ჩათვლით რიცხვები, ხოლო value-ები key-ს შესაბამისი
#    კვადრატები, ანუ {1: 1, 2: 4, 3: 9...}, არ დაწეროთ ხელით, გამოიყენეთ ციკლი(ბონუსი: გამოიყენეთ dictionary comprehension )

# dict1 = {i: i**2 for i in range(1, 11)}
# print(dict1)


# 2. მოცემულია პროდუქტების ლისტი:

# products = [
#     {"cola": {
#         "price": 1.5,
#         "quantity": 10
#     }},
#     {"fanta": {
#         "price": 2.5,
#         "quantity": 5
#     }},
#     {"snickers": {
#         "price": 3.5,
#         "quantity": 12
#     }},
#     {"water": {
#         "price": 4.5,
#         "quantity": 8
#     }},
#     {"beer": {
#         "price": 6.5,
#         "quantity": 5
#     }}
# ]

# ა. დაბეჭდეთ ყველა პროდუქტის დასახელება

# for product in products:
#     for name in product.keys():
#         print(name)

# ბ. გამოითვალეთ ყველა პროდუქტის ღირებულების ჯამი(ანუ პროდუქტის ფასი უნდა გაამრავლოთ რაოდენობაზე და დააჯამოთ)

# total_value = 0

# for product in products:
#     for name, details in product.items():
#         price = details["price"]
#         quantity = details["quantity"]
#         total_value += price * quantity

# print(total_value)

# 3. დაწერეთ პროგრამა, რომელიც მომხმარებელს შეეკითხება ხილის სახელს, მანამ სანამ, მომხმარებელი არ შეიყვანს სიტყვას stop,
#    ამის შემდეგ გამოიტანეთ დიქტის სახით ხილის დასახელება და ველიუ იქნება რამდენჯერაც შეიყვანა ეს ხილი, მაგალითად:

#    Enter your favorite fruit: banana
#    Enter your favorite fruit: apple
#    Enter your favorite fruit: banana
#    Enter your favorite fruit: stop

# შედეგი:

# {'banana': 2, 'apple': 1}

# fruits_count = {}

# while True:
#     fruit = input("Enter your favorite fruit: ")
#     if fruit.lower() == "stop":
#         break
#     fruits_count[fruit] = fruits_count.get(fruit, 0) + 1

# print(fruits_count)