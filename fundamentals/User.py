class User:
    bank_name = "First National Dojo"
    def __init__(self,name,email_address,birthdate,account_number):
        self.name = name
        self.email = email_address
        self.birthdate = birthdate
        self.account_number = account_number
        self.account_balance = 0
        self.savings_balance = 0
    def make_deposit(self, amount):
        self.account_balance += amount
    def make_withdrawal(self,amount):
        self.account_balance -= amount
        
guido = User("Guido van Rossum" ,"Guido@python.com", "Oct 10", "333")
monty = User("Monty Python", "monty@python.com", "Sept 29","323")
george = User("George Washington" ,"george@firstpez.com", "July 4", "1")

guido.make_deposit(100)
print(guido.account_balance)
guido.make_deposit(200)
print(guido.account_balance)
guido.make_deposit(50)
print(guido.account_balance)
guido.make_withdrawal(200)
print(guido.account_balance)

monty.make_deposit(400)
print(monty.account_balance)
monty.make_withdrawal(100)
print(monty.account_balance)
monty.make_withdrawal(100)
print(monty.account_balance)
monty.make_deposit(700)
print(monty.account_balance)

george.make_deposit(900)
print(george.account_balance)
george.make_withdrawal(300)
print(george.account_balance)
george.make_withdrawal(200)
print(george.account_balance)
george.make_withdrawal(100)
print(george.account_balance)


