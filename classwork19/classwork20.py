# დააგენერირეთ სტუდენტის დიქშენერების 100 ელემენტიანი სია
# სახელების, გვარების და იმეილების რენდომულად დასაგენერირებლად
# გამოიყენეთ faker მოდული

# სტუდენტს უნდა ჰქონდეს შემდეგი key-ები და შესაბამისი value-ები:
# student_id - დაიწყოს 1-დან შესაბამისად გაზარდეთ
# first_name - გამოიყენეთ faker
# last_name - გამოიყენეთ faker
# email - გამოიყენეთ faker
# age - 18დან 70 წლამდე(შემთხვევითი პრინციპით)
# is_active - (True ან False) რანდომულად

# არსებული სია json მოდულის დახმარებით ჩაწერეთ ფაილში

# შემდეგ წაიკითხეთ ეს ფაილი json მოდულის დახმარებით, 
# გაფილტრეთ სტუდენტები is_active ქის მიხედვით, ისეთი სტუდენტები რომლის is_active
# არის True, შეიტანეთ ლისტში და ჩაწერეთ ახალ ფაილში

import faker
import json
import random

fake = faker.Faker()

students = []

for i in range(1, 101):
    student = {
        "student_id": i,
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "email": fake.email(),
        "age": random.randint(18, 70),
        "is_active": random.choice([True, False])
    }
    students.append(student)

path1 = "classwork19/students.json"
path2 = "classwork19/active_students.json"

with open(path1, "w") as file:
    json.dump(students, file, indent=4)

with open(path1, "r") as file:
    students_data = json.load(file)

active_students = [student for student in students_data if student["is_active"]]

with open(path2, "w") as file:
    json.dump(active_students, file, indent=4)