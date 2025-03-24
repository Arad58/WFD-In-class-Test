class House:
    def __init__(self, house_number, street, area, number_of_beds, price):
        self.house_number = house_number
        self.street = street
        self.area = area
        self.number_of_beds = number_of_beds
        self.price = price

    def display_attributes(self):
        print(f"House Number: {self.house_number}")
        print(f"Street: {self.street}")
        print(f"Area: {self.area}")
        print(f"Number of Beds: {self.number_of_beds}")
        print(f"Price: €{self.price}")

    def update_house_number(self, new_house_number):
        if isinstance(new_house_number, int):
            self.house_number = new_house_number
        else:
            print("Invalid type for house number. Must be an integer.")

    def update_street(self, new_street):
        if isinstance(new_street, str):
            self.street = new_street
        else:
            print("Invalid type for street. Should be a string.")

    def update_area(self, new_area):
        if isinstance(new_area, str):
            self.area = new_area
        else:
            print("Invalid type for area. Must be a string.")

    def update_number_of_beds(self, new_number_of_beds):
        if isinstance(new_number_of_beds, int):
            self.number_of_beds = new_number_of_beds
        else:
            print("Invalid type for number of beds. Must be an integer.")

    def update_price(self, new_price):
        if isinstance(new_price, (int, float)):
            self.price = new_price
        else:
            print("Invalid type for price. Must be a number.")

class LuxuryHouse(House):
    def __init__(self, house_number, street, area, number_of_beds, price, swimming_pool, garage_capacity):
        super().__init__(house_number, street, area, number_of_beds, price)
        self.swimming_pool = swimming_pool
        self.garage_capacity = garage_capacity

    def display_luxury_attributes(self):
        self.display_attributes()
        print(f"Swimming Pool: {self.swimming_pool}")
        print(f"Garage Capacity: {self.garage_capacity}")

    def update_swimming_pool(self, new_swimming_pool):
        if isinstance(new_swimming_pool, bool):
            self.swimming_pool = new_swimming_pool
        else:
            print("Invalid type for swimming pool. Must be a boolean (True/False).")

    def update_garage_capacity(self, new_garage_capacity):
        if isinstance(new_garage_capacity, int):
            self.garage_capacity = new_garage_capacity
        else:
            print("Invalid type for garage capacity. Must be an integer.")

house_instance = House(42, "Elm Street", "Suburb", 3, 250000)
luxury_house_instance = LuxuryHouse(99, "Oak Avenue", "City Center", 5, 1000000, True, 3)

print("House Details:")
house_instance.display_attributes()

print("\nLuxury House Details:")
luxury_house_instance.display_luxury_attributes()

print("\nUpdating House Attributes:")
house_instance.update_price(260000)
house_instance.update_street("Maple Street")
house_instance.display_attributes()

print("\nUpdating Luxury House Attributes:")
luxury_house_instance.update_swimming_pool(False)
luxury_house_instance.update_garage_capacity(4)
luxury_house_instance.display_luxury_attributes()
