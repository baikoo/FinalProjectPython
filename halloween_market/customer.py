import random

class Customer:
    def __init__(self, name, budget, shopping_list):
        self.name = name
        self.budget = budget
        self.shopping_list = shopping_list

    @classmethod
    def create_with_random_budget(cls, name, shopping_list):
        # ClassMethod to create a customer with a random budget
        budget = random.uniform(30, 100)  # Random budget between 30 and 100
        return cls(name=name, budget=budget, shopping_list=shopping_list)

    def buy_costume(self, shop, costume_name, quantity):
        if costume_name in shop.prices:
            cost = shop.prices[costume_name] * quantity
            if self.check_budget(cost):
                if shop.sell_costume(costume_name, quantity):
                    self.budget -= cost
                    print(f"{self.name} made a purchase {quantity} {costume_name} from {shop.name} shop for {cost:.2f}")
                    print(f"{self.name} budget is {self.budget}")
                    if costume_name in self.shopping_list:
                        self.shopping_list.remove(costume_name)
                else:
                    print(f"{shop.name} is out of stock for {costume_name} or you are asking too much.")
    def check_budget(self, costume_price):
        return self.budget >= costume_price

    def shop_report(self):
        print(f"Customer: {self.name}")
        print(f"  Budget: {self.budget:.2f}")
        print(f"  Shopping List: {self.shopping_list}\n")
