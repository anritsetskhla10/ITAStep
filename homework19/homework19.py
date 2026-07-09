# გვაქვს შემდეგი კლასი და ინსტანსი:

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person: ({self.name}, {self.age})"

p1 = Person("Otar", 35)

# დაწერეთ სერიალაიზერ ფუნქცია, რომელიც დაგეხმარებათ არსებული კლასის ობიექტი გადააქციოთ ისეთ ობიექტად,
# რომ შემდეგ ტექსტურ ფაილში ჩაწეროთ შემდეგი სტრუქტურით:
# Name: Otar, Age: 35

# რათქმაუნდა ჩაწერეთ ფაილში.

# არსებული ფაილიდან წაიკითხეთ ინფორმაცია.

# ასევე დაწერეთ დესერიალაიზერ ფუნქცია, რომელიც ზემოაღნიშნული სტრუქტურის ფაილიდან წაკითხულ ინფორმაციას აქცევს ისევ 
# Person კლასის ობიექტად.(ჩათვალეთ რომ მხოლოდ ერთ ხაზს წერთ ფაილში და წაკითხვითაც ერთ ხაზს კითხულობთ)


def serialize(person, filename):
    with open(filename, 'w') as file:
        file.write(f"Name: {person.name}, Age: {person.age}\n")


def deserialize(filename):
    with open(filename, 'r') as file:
        line = file.readline().strip()
        name, age = line.split(", ")
        name = name.split(": ")[1]
        age = int(age.split(": ")[1])
        return Person(name, age)

print(p1)

file_path = "homework19/person.txt"
serialize(p1, file_path)
p2 = deserialize(file_path)
print(p2)


