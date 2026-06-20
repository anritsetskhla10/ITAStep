# 1. შექმენით მთელი რიცხვების მინიმუმ 5 ელემენტიანი სია, გამოთვალეთ ყველა რიცხვის ჯამი და საშუალო, არ გამოიყენოთ ჩაშენებული ფუნქციები!

# lst1 = [1, 2, 3, 4, 5]
# total = 0
# counter = 0

# for num in lst1:
#     total += num
#     counter += 1

# average = total / counter

# print(f"The sum of the numbers is: {total}")
# print(f"The average of the numbers is: {average}")  

# 2. მოცემულია სია ['a', 'b', 2, 4, 2, 'c', 'j', 1, 'b', 'd', 'c', 4, 1], დაწერეთ ლოგიკა, როემლიც ამ ლისტში დატოვებს უნიკალურ
# ელემენტებს, ანუ არ განმეორდება ელემენტები. არ გამოიყენოთ set!

# lst2 = ['a', 'b', 2, 4, 2, 'c', 'j', 1, 'b', 'd', 'c', 4, 1]
# unique_lst = []

# for item in lst2:
#     if item not in unique_lst:
#         unique_lst.append(item)

# print(unique_lst)

# 3. დააგენერირეთ 20 ელემენტიანი რიცხვების სია, რომელიც შევსებული იქნება -50 დან 50-მდე შემთხვევითი რიცხვებით და შექმენით მეორე 
# სია, რომელიც პირველი სიიდან იქნება შევსებული მხოლოდ ლუწი რიცხვებით და დაბეჭდეთ ორივე სია, გამოიყენეთ აუცილებლად ლისტის გენერატორი!

# import random

# lst3 = [random.randint(-50, 50) for _ in range(20)]
# even_lst = [num for num in lst3 if num % 2 == 0]

# print(f"Original list: {lst3}")
# print(f"Even numbers list: {even_lst}")

# 4. შექმენით ორი ლისტი long_names, short_names

# დაწერეთ პროგრამა რომელიც მომხმარებელს უსასრულოდ შეაყვანინებს სახელებს და შემოყვანილი სახელი თუ 3 სიმბოლოზე მეტი 
# იქნება long_names სახელების ლისტში შეიტანს, ხოლო თუ ნაკლები იქნება short_names-ში

# ლისტში უნდა ჩაიყაროს სახელები ისე, რომ პირველი ასოები იყოს დიდი, 
# მაგალითად, მომხმარებელი თუ შემოიყვანს ასეთი სახით "daVit" ან "davit", ლისტში უნდა შეინახოთ "Davit"
# ასევე, თავსა და ბოლოში მოაშორეთ ცარიელი ადგილები!

# პროგრამა ჩერდება იმ შემთხვევაში, მომხმარებელი თუ შეიყვანს სიტყვას stop ან Stop ან exit ან Exit ან quit ან Quit

# long_names = []
# short_names = []

# while True:
#     name = input("Enter a name (type 'stop', 'exit', or 'quit' to end): ")
#     if name.lower() in ['stop', 'exit', 'quit']:
#         break
#     name = name.strip()
#     if len(name) > 3:
#         long_names.append(name.capitalize())
#     else:
#         short_names.append(name.capitalize())

# print(f"Long names: {long_names}")
# print(f"Short names: {short_names}")
