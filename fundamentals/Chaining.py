class User:
    bank_name = "First National Dojo"
    def __init__(self,name,email_address,birthdate,account_number):
        self.name = name
        self.email = email_address
        self.account_balance = 0
    def make_deposit(self, amount):
        self.account_balance += amount
        return self
    def make_withdrawal(self,amount):
        self.account_balance -= amount
        return self
        
guido = User("Guido van Rossum" ,"Guido@python.com", "Oct 10", "333")
monty = User("Monty Python", "monty@python.com", "Sept 29","323")
george = User("George Washington" ,"george@firstpez.com", "July 4", "1")

guido.make_deposit(100).make_deposit(200).make_deposit(300).make_withdrawal(50)
print(guido.account_balance)

monty.make_deposit(200).make_deposit(100).make_withdrawal(200).make_deposit(400)
print(monty.account_balance)

george.make_deposit(900).make_deposit(800).make_withdrawal(400).make_deposit(300)
print(george.account_balance)