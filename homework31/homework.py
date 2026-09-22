# MongoDB-ში შექმენით ბაზა დასახელებით 'shop', შექმენით კოლექცია 'products'.
# დაწერეთ პითონის სკრიპტი, რომელიც დაუკავშირდება ამ ბაზას და products კოლექციაში შეიტანეთ მონაცემები შემდეგნაირად:
# პითონის კოდშივე დააგენერირეთ 50 პროდუქტი, რომელსაც გააჩნია შემდეგი სახე:

# name → "Product 1", "Product 2" … "Product 50"
# category → "Electronics", "Books", "Clothes" - აქედან ერთ-ერთი შემთხვევითობით
# price → შემთხვევითი რიცხვი (50 – 3000)
# quantity → შემთხვევითი რიცხვი (0 – 100)
# available → False თუ რაოდენობა იქნება 0, სხვა შემთხვევაში True

# დაბეჭდეთ ყველა პროდუქტი
# დაბეჭდეთ მხოლოდ ხელმისაწვდომი პროდუქტები
# დაბეჭდეთ პროდუქტები, რომლის ფასი მეტია 1000-ზე
# დაითვლეთ  რამდენი პროდუქტია თითო კატეგორიაში
# ერთ-ერთ პროდუქტს შეუცვალეთ რაოდენობა

import random
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["shop"]
products_col = db["products"]

products_col.delete_many({})

categories = ["Electronics", "Books", "Clothes"]
products = []

for i in range(1, 51):
    quantity = random.randint(0, 100)
    products.append({
        "name": f"Product {i}",
        "category": random.choice(categories),
        "price": random.randint(50, 3000),
        "quantity": quantity,
        "available": quantity > 0
    })

products_col.insert_many(products)

for p in products_col.find():
    print(p)

for p in products_col.find({"available": True}):
    print(p)

for p in products_col.find({"price": {"$gt": 1000}}):
    print(p)

pipeline = [
    {
        "$group": {
            "_id": "$category",
            "count": {"$sum": 1}
        }
    }
]

for item in products_col.aggregate(pipeline):
    print(item["_id"], item["count"])

products_col.update_one(
    {"name": "Product 1"},
    {
        "$set": {
            "quantity": 25,
            "available": True
        }
    }
)

print(products_col.find_one({"name": "Product 1"}))

client.close()