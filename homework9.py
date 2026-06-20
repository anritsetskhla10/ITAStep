# 1. დაწერეთ ფუნქცია, რომელიც პარამეტრად მიიღებს რიცხვს, თუ რამდენჯერ უნდა ჰკითხოს მომხმარებელს რიცხვი და საბოლოოდ დააჯამებს
#    ყველა შეყვანილ რიცხვს, თუ არგუმენტად არ გადაეცა არანაირი რიცხვი, მაშინ ფუნქციამ 5-ჯერ ჰკითხოს მომხმარებელს რიცხვის 
#    შეყვანა და დააჯამოს ეს 5 რიცხვი. დააბრუნეთ საბოლოო ჯამი

# def sum_numbers(count=5):

#     total = 0
#     for _ in range(count):
#         try:
#             num = int(input("Enter a number: "))
#         except ValueError:
#             print("Invalid input. Please enter a valid integer.")
#             num = int(input("Enter a number: "))
#         total += num
#     return total

# print(sum_numbers(3))
# print(sum_numbers())


# 2. დაწერეთ ფუნქცია რომელიც მიიღებს არგუმენტების განუსაზღვრელ რაოდენობას მთელი რიცხვების სახით და დააბრუნებს
#    ორ ლისტს, ერთ ლისტში იქნება გადაცმული არგუმენტებიდან კენტი რიცხვები ხოლო მეორე ლისტში ლუწი რიცხვები

# def separate_even_odd(*args):
#     even_numbers = []
#     odd_numbers = []
#     for num in args:
#         if num % 2 == 0:
#             even_numbers.append(num)
#         else:
#             odd_numbers.append(num)
#     return f'Even numbers: {even_numbers}, Odd numbers: {odd_numbers}'

# print(separate_even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

# 3. დაწერეთ ფუნქცია, რომელსაც პარამეტრად გადაეცემა მომხმარებლის მიერ შეყვანილი წინადადება და ამ წინადადებაში დაითვლის სიტყვებს
#    და დიქტის სახით დააბრუნებს თუ რომელი სიტყვა რამდენჯერ არის, მაგ: "This is a test. This test is fun." --> დააბრუნებს დიქტის
#    შემდეგი სახით: {'this': 2, 'is': 2, 'a': 1, 'test': 2, 'fun': 1} უნდა იყოს case insensitive (ანუ დიდ და პატარა ასოებს არ უნდა
#    ჰქონდეს მნიშვნელობა!)

# def count_words(sentence):
#     words = sentence.lower().split()
#     word_count = {}
#     for word in words:
#         word = word.strip('.,!?";()')  
#         if word in word_count:
#             word_count[word] += 1
#         else:
#             word_count[word] = 1
#     return word_count

# print(count_words("This is a test. This test is fun."))