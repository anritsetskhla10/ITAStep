# 1. დაწერეთ პროგრამა, რომელიც მომხმარებელს შემოაყვანინებს წინადადებას, პირველ სიტყვას და მეორე სიტყვას და შემოყვანილ წინადადებაში
# პირველ სიტყვას ჩაანაცვლებს მეორე სიტყვით

sentence = input("Enter a sentence: ")
first_word = input("Enter the first word: ")
second_word = input("Enter the second word: ")

new_sentence = sentence.replace(first_word, second_word)
print(new_sentence)


# 2. დაწერეთ პროგრამა, რომელიც მომხმარებლის მიერ შემოყვანილ წინადადებაში იპოვის ყველაზე გრძელ სიტყვას და დაბეჭდავს მას. არ გამოიყენოთ max() ფუნქცია!

sentence2 = input("Enter a sentence: ")
words = sentence2.split()
longest_word = ""

for word in words:
    if len(word) > len(longest_word):
        longest_word = word

print(f"The longest word is: {longest_word}")

# 3. დაწერეთ პროგრამა, რომელიც მომხმარებელს შეეკითხება ორ სიტყვას შეამოწმებს არის თუ არა ერთმანეთის ანაგრამა
# ანაგრამა არის ერთ სიტყვაში ასოების გადაადგილებით მიღებული მეორე სიტყვა, მაგალითად ("listen", "silent" ), ("Triangle", "Integral")
# და ა.შ. უნდა იყოს case-insensitive, ანუ მომხმარებელი დიდი ასოებით შემოიყვანს თუ არა ტექსტს, არ უნდა ჰქონდეს მნიშვნელობა.
# არ გამოიყენოთ sorted() ფუნქცია!

word1 = input("Enter the first word: ").lower()
word2 = input("Enter the second word: ").lower()

is_anagram = True

if len(word1) != len(word2):
    is_anagram = False
else:
    for char1 in word1:
        found = False
        temporary_word2 = ""  
        
        for char2 in word2:
            if char2 == char1 and not found:
                found = True  
            else:
                temporary_word2 += char2  

        if not found:
            is_anagram = False
            break

        word2 = temporary_word2

if is_anagram and word2 == "":
    print("they are anagrams.")
else:
    print("they are not anagrams.")