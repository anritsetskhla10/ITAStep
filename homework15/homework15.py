# შექმენით ბანკის სისტემა, რომელიც შეიცავს მომხმარებლებს და მათ ანგარიშებს. სისტემაში უნდა გამოიყენოთ:
#    კლასის ატრიბუტები:
#    	bank_name - ბანკის დასახელება
#    	total_accounts(private) - ანგარიშების რაოდენობა(ყოველი ანგარიშის გახსნის შემდეგ ავტომატურად უნდა გაიზარდოს)
   	
#    ინსტანსის ატრიბუტები:
# 	owner (protected) — ანგარიშის მფლობელის სახელი
# 	balance (private) — ანგარიშზე არსებული თანხა
# 	account_number (private) — უნიკალური ანგარიში(ეს არ უნდა გადაეცეს ობიექტის შექმნის დროს, უნდა დაგენერირდეს
# 	ავტომატურად შემდეგი პრინციპით: პირველი ექაუნთის ნომერი იქნება AN0001, მეორესი AN0002 და ა.შ.
	
#    მეთოდები:
#    	__init__(self, owner, balance) — მნიშვნელობების მინიჭება

# 	deposit(self, amount) - ბალანსზე თანხის დამატება

# 	withdraw(self, amount) - ბალანსიდან თანხის გამოტანა

# 	check_balance(self) — აბრუნებს ბალანსს

# 	get_account_number(self) — აბრუნებს ანგარიშის ნომერს

# 	change_owner(self, new_owner) — ცვლის owner მნიშვნელობას
	
#    კლასის მეთოდი:
#    	get_total_accounts(): — აბრუნებს ანგარიშების რაოდენობას

#    სტატიკური მეთოდი:
#    	validate_amount(amount): — აბრუნებს True, თუ თანხა დადებითია
#    	ეს მეთოდი უნდა გამოიყენოთ __init__-ში ბალანსის შემოწმებისას და ისე გაუკეთოთ ბალანსს ინიციალიზაცია. ასევე, 	deposit და withdraw დროსაც ეს გამოიყენეთ რომ ვალიდაცია გაუკეთოთ amount-ს და ისე დაუმატოთ ან გამოიტანოთ თანხა
   	
# ობიექტი დაბეჭდვისას გამოჩნდეს შემდეგი სახით, მაგალითად: "Account: AN0002 | Owner: Nino Beridze"

class BankAccount:
    bank_name = "MyBank"
    __total_accounts = 0

    def __init__(self, owner, balance):
        self._owner = owner
        if self.validate_amount(balance):
            self.__balance = balance
        else:
            raise ValueError("Initial balance must be a positive amount.")
        BankAccount.__total_accounts += 1
        self.__account_number = f"AN{BankAccount.__total_accounts:04d}"

    def deposit(self, amount):
        if self.validate_amount(amount):
            self.__balance += amount
        else:
            raise ValueError("Deposit amount must be a positive number.")

    def withdraw(self, amount):
        if self.validate_amount(amount):
            if amount <= self.__balance:
                self.__balance -= amount
            else:
                raise ValueError("Insufficient funds for withdrawal.")
        else:
            raise ValueError("Withdrawal amount must be a positive number.")

    def check_balance(self):
        return self.__balance

    def get_account_number(self):
        return self.__account_number

    def change_owner(self, new_owner):
        self._owner = new_owner

    @classmethod
    def get_total_accounts(cls):
        return cls.__total_accounts

    @staticmethod
    def validate_amount(amount):
        return amount > 0

    def __str__(self):
        return f"Account: {self.__account_number} | Owner: {self._owner}"


account1 = BankAccount("Anri Tsetskhlashvili", 1000)
account2 = BankAccount("Nino Beridze", 500)

print(account1)
print(account2)  

account1.deposit(500)
print(f"{account1.get_account_number()} new balance after deposit: {account1.check_balance()}")

account1.withdraw(300)
print(f"{account1.get_account_number()} new balance after withdrawal: {account1.check_balance()}")

account2.change_owner("Giorgi Beridze")
print(f"changed owner: {account2}")

print(f"Bank name: {BankAccount.bank_name}")
print(f"Total accounts created: {BankAccount.get_total_accounts()}")

try:
    account1.withdraw(2000)
except ValueError as e:
    print(f"System error: {e}")