# 1. დაწერეთ ტრანზაქციის ფუნქცია, რომელსაც გადაეცემა ატრიბუტად ბალანსი და გადასახდელი თანხა, დაუწერეთ დეკორატორი, 
# რომელიც საკომისიოს ჩამოაჭრის 1 ლარს და თუ საკმარისი თანხა არ იქნება ანგარიშზე დაუბრუნეთ შეცდომის ტექსტი

def fee_decorator(func):
    def wrapper(self, amount):
        fee = 1
        total_required = amount + fee
        
        if self.balance < total_required:
            return "Error: Insufficient funds"
        
        self.balance -= fee
        
        return func(self, amount)
        
    return wrapper


class Transaction:
    def __init__(self, balance):
        self.balance = balance

    @fee_decorator
    def process_payment(self, amount):
        self.balance -= amount
        return f"Transaction successful. New balance: {self.balance}"


def run_tests():
    print("testing Transaction class with fee_decorator")
    
    # წარმატებული ტრანზაქცია
    account1 = Transaction(10)
    result1 = account1.process_payment(5)
    print(f"Test 1 (10 balance, 5 payment): {result1}")
    assert account1.balance == 4, "Test 1 Failed!"

    # არასაკმარისი თანხა
    account2 = Transaction(5)
    result2 = account2.process_payment(5)
    print(f"Test 2 (5 balance, 5 payment): {result2}")
    assert result2 == "Error: Insufficient funds", "Test 2 Failed!"

    # ზუსტად სამყოფი თანხა
    account3 = Transaction(6)
    result3 = account3.process_payment(5)
    print(f"Test 3 (6 balance, 5 payment): {result3}")
    assert account3.balance == 0, "Test 3 Failed!"
    
    print("tests completed!")

run_tests()
        

# 2. შექმენით მეტაკლასი, რომელიც სხვა კლასზე გამოყენების შემთხვევაში შეამოწმებს ამ კლასის მეთოდის სახელებს,
#    შემდეგი სახით: თუ მეთოდი იწყება _ ეს მეთოდი ვალიდური იქნება, თუ არ იწყება _, მაშინ აღზევდეს 
#    ValueError. მაგ: _test() - ეს მეთოდი იქნება ვალიდური, test() - ეს მეთოდი არ იქნება ვალიდური
#    და გამოიწვევს ValueError-ს. გაითვალისწინეთ რომ მეტაკლასმა უნდა შეამოწმოს მხოლოდ მეთოდები და არა ატრიბუტები!

class MethodCheckerMeta(type):
    def __new__(cls, name, bases, class_dict):
        
        for attr_name, attr_value in class_dict.items():
            if callable(attr_value):
                if not attr_name.startswith('_'):
                    raise ValueError(f"Method '{attr_name}' in class '{name}' must start with '_'.")
        
        return super().__new__(cls, name, bases, class_dict)


class ValidClass(metaclass=MethodCheckerMeta):
    
    def __init__(self):
        self.balance = 0
        
    def _test(self):
        return "This is a valid method"



try:
    class InvalidClass(metaclass=MethodCheckerMeta):
        def test(self):
            pass
            
except ValueError as e:
    print(f"Error occurred: {e}")
