class CostumeShop:
    def __init__(self, name):
        self.name = name
        self.costumes = {}
        self.prices = {}
        self.demand = {}

    @classmethod
    def create_shop_with_costumes(cls, name, inventory):
        # ClassMethod to create a shop with the inventory
        shop = cls(name)
        for costume, details in inventory.items():
            shop.add_costume(costume, details["stock"], details["price"])
        return shop

    def add_costume(self, costume_name, stock, price):
        self.costumes[costume_name] = stock
        self.prices[costume_name] = price
        self.demand[costume_name] = 0

    def adjust_price(self, costume_name, new_price):
        if costume_name in self.prices:
            self.prices[costume_name] = new_price

    def adjust_stock(self, costume_name, new_stock):
        if costume_name in self.costumes:
            self.costumes[costume_name] = new_stock

    def adjust_demand(self, costume_name, population):
        if costume_name in self.demand:
            self.demand[costume_name] += population

    def sell_costume(self, costume_name, quantity):
        if costume_name in self.costumes and self.costumes[costume_name] >= quantity:
            self.costumes[costume_name] -= quantity
            self.demand[costume_name] += quantity
            self.adjust_demand(costume_name, quantity)
            if self.demand[costume_name] > 10:
                self.adjust_price(costume_name, self.prices[costume_name] + 0.1)
            return True
        return False

    def report_stock(self):
        print(f"Shop: {self.name}")
        for costume_name in self.costumes:
            print(f"  {costume_name}: Stock = {self.costumes[costume_name]}, "
                  f"Price = {self.prices[costume_name]:.2f}, Demand = {self.demand[costume_name]}")
        print("\n")
