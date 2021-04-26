# class Budget:
#     pass

# obj = Budget()
# print(type(obj))

# class Budget:
    
#     amount = 0

#     def_init_(self):
#         self.category = ["Food", "Clothing", "Entertainment"]


class Budget:

    def __init__ (self, Food, Clothing):
        self.category = Food
        self.amount = Clothing

    #methods

    def check_balance(self):
        #pass
        return 'Hello, This is a check balance confirmation, You have a $2000 total balance'

    def deposit(self):
        #pass
        return 'Hello, This is a deposit confirmation, You have deposited $1000'

    def current_balance_after_deposit(self):
        #pass
        return 'Hello, This is a balance confirmation after your $1000 deposit, your balance is now $3000'

    def transfer(self):
        #pass
        return 'Hello, This is a transfer confirmation, You can make a transfer tommorrow'

    def withdraw(self):
        #pass
        return 'Hello, This is a withdraw confirmation, You have withdrew $500'

    def check_balance_after_withdrawal(self):
        #pass
        return 'Hello, This is your balance confirmation after withdrawing $500, You now have a $2500 total balance'


category =  Budget("Clothing", 500)    
category_1 = Budget ("Food", 500)    
category_2 = Budget ("Entertainment", 500)    

print(category.check_balance())
print(category.deposit())
print(category.current_balance_after_deposit())
print(category.transfer())
print(category.withdraw())
print(category.check_balance_after_withdrawal())




