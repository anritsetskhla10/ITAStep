# 1. დაწერეთ პროგრამა, რომელიც მომხმარებელს უსასრულოდ შეეკითხება ჯერ სახელს, შემდეგ გვარს და რაიმე ფაილში ჩაწერს 
#    სახელს და გვარს ერთ ხაზზე თავისი ნუმერაციით, ყველა ახალი სახელი და გვარი უნდა იყოს ახალ ხაზზე ჩაწერილი, მაგალითად:
   
#    Enter your first name: Otar
#    Enter your last name: Tumanishvili
#    Enter your first name: Nika
#    Enter your last name: Papaskiri
#    Enter your first name: stop

#    ფაილში უნდა ჩაიწეროს შემდეგი სახით:
#    1. Otar Tumanishvili
#    2. Nika Papaskiri


#    პროგრამა ჩერდება იმ შემთხევაში, თუ მომხმარებელმა სახელის ადგილას შეიყვანა სიტყვა stop
# with open("names.txt", "w") as file:
#     pass

# counter = 1

# while True:
#     first_name = input("Enter your first name: ").strip()
    
#     if first_name.lower() == "stop":
#         break
        
#     if first_name == "":
#         print("First name cannot be empty. Please try again.")
#         continue
        
#     last_name = input("Enter your last name: ").strip()
    
#     if last_name == "":
#         print("Last name cannot be empty. Please try again.")
#         continue

#     with open("names.txt", "a") as file:
#         file.write(f"{counter}. {first_name} {last_name}\n")
    
#     counter += 1


# 2. თანდართულ ფაილში "persons.txt" მოცემულია ადამიანების სია შემდეგი ფორმატით:
#    სახელი და გვარი, ასაკი, ქალაქი

#    Evelyn Cook, 75, Nixonland
#    Dr. Briana Davidson, 22, South Hunterside
#    ...
#    ...

#    თქვენი დავალებაა არსებული ფაილიდან წაიკითხოთ ინფორმაცია, შექმნათ ორი ახალი ტექსტური ფაილი (.txt გაფართოებით), ერთ ფაილში
#    ჩაწერეთ ყველა პიროვნება რომლის ასაკი ნაკლებია 50-ზე, ხოლო მეორე ფაილში ჩაწერეთ ყველა პიროვნება, რომლის ასაკი მეტია 50-ზე,
#    ფორმატი დაცული უნდა იყოს ისეთი სახით, როგორიც არის ორიგინალ "persons.txt" ფაილში ანუ თითო პიროვნება თითო ხაზზე!

# with open("persons.txt", "r") as file:
#     lines = file.readlines()

# with open("under_50.txt", "w") as under_50_file, open("over_50.txt", "w") as over_50_file:
#     for line in lines:
#         parts = line.strip().split(", ")
#         if len(parts) != 3:
#             continue  
        
#         name, age_str, city = parts
#         try:
#             age = int(age_str)
#         except ValueError:
#             continue 
        
#         if age < 50:
#             under_50_file.write(line)
#         else:
#             over_50_file.write(line)

