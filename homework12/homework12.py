# 1. დაწერეთ ფუნქცია, რომელიც ატრიბუტად მიიღებს რიცხვს, რა რიცხვსაც გადავცემთ, იმდენჯერ შეეკითხება მომხმარებელს 
#    სახელს, გვარს და ასაკს. ანუ თუ გადავეცით 3, 3-ჯერ შეეკითხება მომხმარებელს აღნიშნულ ინფორმაციას, ინფუთის 
#    საფუძველზე csv ფაილში ჩაწერეთ შესაბამისი ინფორმაცია შემდეგი სახით, მაგალითად:

#    ID,first_name,last_name,age
#    1,John,Doe,25
#    2,Alice,White,30

#    და ა.შ.
   
#    გამოიყენეთ try, ecxept იმისათვის რომ მომხმარებელმა ასაკის შემოყვანის დროს აუცილებლად ინტეჯერი შემოიყვანოს!
#    ფაილში ჩასაწერად აუცილებლად გამოიყენეთ csv მოდულიდან writer და DictWriter!

# import csv

# def write_persons_to_csv(num_persons):

#     with open('persons.csv', mode='w', newline='') as file:
#         fieldnames = ['ID', 'first_name', 'last_name', 'age']
#         writer = csv.DictWriter(file, fieldnames=fieldnames)
#         writer.writeheader()

#         for i in range(1, num_persons + 1):
#             first_name = input(f"Enter first name for person {i}: ")
#             last_name = input(f"Enter last name for person {i}: ")
#             while True:
#                 try:
#                     age = int(input(f"Enter age for person {i}: "))
#                     break
#                 except ValueError:
#                     print("Please enter a valid integer for age.")

#             writer.writerow({'ID': i, 'first_name': first_name, 'last_name': last_name, 'age': age})

# write_persons_to_csv(3)


# 2. მიმაგრებულ students.csv ფაილიდან წაიკითხეთ ინფორმაცია, გაფილტრეთ Grade-ის მიხედვით შემდეგნაირად:
#    ყველა სტუდენტი, რომელსაც 50-ზე ნაკლები ქულა აქვს შეინახეთ ახალ ფაილში(failed_students.csv)
#    ყველა სტუდენტი, რომელსაც 50-ზე მეტი ქულა აქვს შეინახეთ ახალ ფაილში(passed_students.csv)

#    ფაილებიდან ინფორმაციის წასაკითხად და ჩასაწერად აუცილებლად გამოიყენეთ DictReader და DictWriter!

# import csv

# with open('students.csv', mode='r', newline='') as file:
#     reader = csv.DictReader(file)
    
#     original_fieldnames = reader.fieldnames  
    
#     failed_students = []
#     passed_students = []
    
#     for row in reader:
#         try:
#             if 'Grade' not in row or not row['Grade']:
#                 continue
                
#             grade = int(row['Grade'])
            
#             if grade < 50:
#                 failed_students.append(row)
#             else:
#                 passed_students.append(row)
#         except ValueError:
#             student_name = row.get('Name', 'Unknown')
#             print(f"Invalid grade for student {student_name}. Skipping.")

# with open('failed_students.csv', mode='w', newline='') as failed_file, open('passed_students.csv', mode='w', newline='') as passed_file:
     
#     failed_writer = csv.DictWriter(failed_file, fieldnames=original_fieldnames)
#     passed_writer = csv.DictWriter(passed_file, fieldnames=original_fieldnames)

#     failed_writer.writeheader()
#     passed_writer.writeheader()

#     failed_writer.writerows(failed_students)
#     passed_writer.writerows(passed_students)