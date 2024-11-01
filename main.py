from halloween_market.city import City
from halloween_market.shop import CostumeShop
from halloween_market.customer import Customer

# Initialization the city using class method
city = City.create_default_city()

# Defining costumes for shops
costumes_in_shop_one = {
        "Dracula": {"stock": 30, "price": 25.0},
        "Ghost Casper": {"stock": 40, "price": 15.0},
        "Zombie": {"stock": 20, "price": 22.0},
        "Vampire": {"stock": 25, "price": 30.0},
    }
costumes_in_shop_two = {
        "Doodle": {"stock": 50, "price": 20.0},
        "Ghost Casper": {"stock": 40, "price": 15.0},
        "Vampire": {"stock": 25, "price": 30.0},
        "Tom and Jerry": {"stock": 35, "price": 18.0}
    }
# Creating shops with costumes using class methods
shop_one = CostumeShop.create_shop_with_costumes("Whoo-Whoo", costumes_in_shop_one)
shop_two = CostumeShop.create_shop_with_costumes("Hallo Wee", costumes_in_shop_two)

# Adding shops to the city
city.add_shop(shop_one)
city.add_shop(shop_two)

# Simulating the demand in the city based on population
city.simulate_demand()

# Creating customers with random budgets using class methods
customer_one = Customer.create_with_random_budget("Lisa", ["Zombie", "Ghost Casper"])
customer_two = Customer.create_with_random_budget("Bob", ["Dracula", "Tom and Jerry"])

# Customers buying the costumes
customer_one.buy_costume(shop_one, "Zombie", 1)
customer_one.buy_costume(shop_two, "Dracula", 1)

customer_two.buy_costume(shop_two, "Tom and Jerry", 1)
customer_two.buy_costume(shop_one, "Ghost Casper", 2)

# Generating reports
print("\n")
city.report()
customer_one.shop_report()
customer_two.shop_report()


