import random
from halloween_market.shop import CostumeShop

class City:
    def __init__(self, name, population):
        self.name = name
        self.population = population
        self.costume_shops = []

    @classmethod
    def create_default_city(cls):
        # ClassMethod to create a city with a default name and population
        return cls(name="Delulu City", population=5000)

    def add_shop(self, shop):
        self.costume_shops.append(shop)

    def simulate_demand(self):
        for shop in self.costume_shops:
            for costume_name in shop.costumes:
                demand_increase = int(random.uniform(1, self.population / 100))
                shop.adjust_demand(costume_name, demand_increase)

    def report(self):
        print(f"Report for {self.name}:\n")
        for shop in self.costume_shops:
            shop.report_stock()
