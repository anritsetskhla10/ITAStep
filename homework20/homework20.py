# მოცემულია persons.json ფაილი შემდეგი სტრუქტურით:
# [
#     {
#         "id": 1,
#         "name": "Ana",
#         "age": 19
#     },
#     {
#         "id": 2,
#         "name": "Bob",
#         "age": 21
#     }
# ]

# თქვენი დავალებაა დაწეროთ ფუნქცია, რომელსაც პარამეტრად გადაეცემა რიცხვი და გადაცემული რიცხვის საფუძველზე 
# იმდენჯერ ჰკითხავს მომხმარებელს სახელს და ასაკს, შემდეგ კი persons.json ფაილში დაამატებს ახალ პერსონებს
# თავისივე აიდებით.მაგალითათ ორჯერ ვეკითხებით მომხმარებელს:

# enter your name: Walter
# enter your age: 45
# enter your name: Niko
# enter your age: 32

# persons.json უნდა გამოიყურებოდეს შემდეგნაირად:

# [
#     {
#         "id": 1,
#         "name": "Ana",
#         "age": 19
#     },
#     {
#         "id": 2,
#         "name": "Bob",
#         "age": 21
#     },
#     {
#         "id": 3,
#         "name": "Walter",
#         "age": 45
#     },
#     {
#         "id": 4,
#         "name": "Niko",
#         "age": 32
#     }
# ]

# გაითვალისწინეთ! არ უნდა დაირღვეს json ფაილის სტრუქტურა, ანუ პერსონები უნდა იყოს ლისტში, ლისტის გარეთ არ ჩაამატოთ!
# ასევე, აიდები უნდა გაგრძელდეს ბოლო აიდის მქონე პერსონის შემდეგ ლოგიკურად, ანუ json ფაილში თუ ბოლო პერსონის აიდი იქნება 2, 
# ახალი პერსონის დამატებისას აიდი უნდა იყოს 3, თუ ბოლო პერსონის აიდი იქნება 5, ახალი პერსონის უნდა იყოს 6 და ასე შემდეგ!


import json
import os

def add_persons(num):
    if os.path.exists('homework20/persons.json'):
        try:
            with open('homework20/persons.json', 'r', encoding='utf-8') as file:
                persons = json.load(file)
                print(persons)
        except json.JSONDecodeError:
            persons = []
    else:
        persons = []

    last_id = persons[-1]['id'] if persons else 0

    for _ in range(num):
        name = input("Enter your name: ")

        while True:
            try:
                age = int(input("Enter your age: "))
                break 
            except ValueError:
                print("Invalid input. Please enter a valid number for age.")
        
        last_id += 1
        new_person = {
            "id": last_id,
            "name": name,
            "age": age
        }
        persons.append(new_person)

    with open('homework20/persons.json', 'w', encoding='utf-8') as file:
        json.dump(persons, file, indent=4, ensure_ascii=False)


add_persons(2)    