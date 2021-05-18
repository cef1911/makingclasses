self.category = ["Food", "Clothing", "Entertainment"]


class Category:

    #constructor
    def __init__ (self, category, amount):
        self.category = category
        self.amount = amount
        

    #methods
    def deposit(self, amount):
   
        self.amount += amount
        return "You have successfully deposited {} in the {} category".format(amount, self.category)

    def budget_balance(self):
        return "This is the current balance: {}".format(self.amount)
    
    def check_balance(self):
      
        return "This is the check balance: {}".format(self.amount)

    def withdraw(self, amount):
       
        self.amount -= amount
        return "You have successfully withdrew {} in the {} category".format(amount, self.category)

    def transfer(self, amount, category):
        category.amount -= amount
        self.amount += amount
        return "You have successfully transferred {} in {} category to {} category".format(amount, category.category, self.category)
       

    
    

food_category = Category ("Food", 500)    
clothing_category = Category ("Clothing", 300)    
car_category = Category ("Car Expenses", 600)    

print(food_category.deposit(250))
print(food_category.budget_balance())
#print(category.deposit())

print(clothing_category.deposit(300))
print(clothing_category.check_balance())

print(car_category.withdraw(400))
print(car_category.budget_balance())


print(car_category.transfer(200, food_category))


   




