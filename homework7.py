# 1. მოცემულია სია:

# (სახელი, გვარი, ასაკი)


# persons = [
#     ('Kelly', 'Simpson', 26),
#     ('Erika', 'Stephens', 24),
#     ('Cheryl', 'Dunn', 30),
#     ('Amy', 'Larsen', 49),
#     ('Christine', 'Gordon', 23),
#     ('Monica', 'Huff', 38),
#     ('David', 'Nixon', 36),
#     ('Cindy', 'Escobar', 41),
#     ('Cindy', 'White', 33), 
#     ('Joel', 'Hall', 43),
#     ('Steven', 'Winters', 28),
#     ('Alex', 'Cole', 68),
#     ('Alex', 'Smith', 32),
#     ('Brittany', 'Thompson', 18),
#     ('Ernest', 'Young', 43),
#     ('Traci', 'Wells', 38),
#     ('Andrew', 'Flores', 61),
#     ('Christopher', 'Lewis', 29),
#     ('Kevin', 'Willis', 57),
#     ('Kayla', 'Lucas', 28),
#     ('Michelle', 'Rush', 43),
#     ('Thomas', 'Mason', 37)
# ]

# დაწერეთ უსასრულო ციკლი, რომელშიც მომხმარებელს ჰკითხავთ სახელს, თუ სახელი იქნება მოცემულ სიაში, შემდეგ ჰკითხეთ გვარი და გვარიც თუ იქნება,
# დაბეჭდეთ მისი ასაკი, ხოლო თუ არ იქნება სახელი დაბეჭდეთ რომ არ არის მოცემული სახელი, შესაბამისად გვარი აღარ ჰკითხოთ, ანალოგიურად
# მოიქეცით გვარის კითხვის შემთხვევაშიც. ციკლი უნდა გაჩერდეს იმ შემთხვევაში თუ მომხმარებელი შემოიყვანს სიტყვას "stop".

# while True:
#     name = input("Enter a name (type 'stop' to exit): ")
#     if name.lower() == "stop":
#         break

#     name_found = False

#     for person in persons:
#         if person[0].lower() == name.lower():
#             name_found = True
#             break
            
#     if not name_found:
#         print(f"Name '{name}' is not found.")
#     else:
#         surname = input("Enter a surname: ")
#         person_found = False
        
#         for person in persons:
#             if person[0].lower() == name.lower() and person[1].lower() == surname.lower():
#                 print(f"{person[0]} {person[1]} is {person[2]} years old.")
#                 person_found = True
#                 break
                
#         if not person_found:
#             print(f"{name} is found, but the surname '{surname}' does not match.")

# 2. დაწერეთ პროგრამა, რომელიც მომხმარებელს შემოაყვანინებს ჯერ პირველ და მერე მეორე სიტყვას.
#    იპოვეთ ამ სიტყვებში საერთო სიმბოლოები, განსხვავებული სიმბოლოები, და გაერთიანებული სიმბოლოები(ანუ ორივეში ერთად რომელიცაა ყველა ერთად)
#    დაბეჭდეთ ყველა ზემოთჩამოთვლილი(გამოიყენეთ set)

# word1 = input("Enter the first word: ")
# word2 = input("Enter the second word: ")

# common_letters = set(word1) & set(word2)
# different_letters = set(word1) ^ set(word2)
# combined_letters = set(word1) | set(word2)

# print(f"Common letters: {common_letters}")
# print(f"Different letters: {different_letters}")
# print(f"Combined letters: {combined_letters}")