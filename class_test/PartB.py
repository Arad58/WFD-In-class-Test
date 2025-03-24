import unittest
from PartA import House, LuxuryHouse

class TestHouse(unittest.TestCase):

    def test_instance_of_class(self):
        house = House(42, "Elm Street", "Suburb", 3, 250000)
        self.assertIsInstance(house, House)

    def test_not_instance_of_class(self):
        luxury_house = LuxuryHouse(99, "Oak Avenue", "Suburb", 5, 1000000, True, 3)
        self.assertNotIsInstance(luxury_house, int)

    def test_objects_identical(self):
        house1 = House(42, "Elm Street", "Suburb", 3, 250000)
        house2 = house1
        self.assertIs(house1, house2)

    def test_objects_not_identical(self):
        house1 = House(42, "Beef Street", "Suburb", 2, 250000)
        house2 = House(42, "Beef Street", "Suburb", 2, 250000)
        self.assertIsNot(house1, house2)

    def test_update_house_number(self):
        house = House(42, "Elm Street", "Suburb", 3, 250000)
        house.update_house_number(50)
        self.assertEqual(house.house_number, 50)

    def test_update_street(self):
        house = House(42, "Elm Street", "Suburb", 3, 250000)
        house.update_street("Maple Street")
        self.assertEqual(house.street, "Maple Street")

    def test_update_price_invalid_type(self):
        house = House(42, "Elm Street", "Suburb", 3, 250000)
        house.update_price("invalid")
        self.assertNotEqual(house.price, "invalid")

class TestLuxuryHouse(unittest.TestCase):

    def test_update_swimming_pool(self):
        luxury_house = LuxuryHouse(99, "Green Avenue", "Suburb", 5, 1000000, True, 3)
        luxury_house.update_swimming_pool(False)
        self.assertFalse(luxury_house.swimming_pool)

    def test_update_garage_capacity(self):
        luxury_house = LuxuryHouse(99, "Green Avenue", "Suburb", 5, 1000000, True, 3)
        luxury_house.update_garage_capacity(4)
        self.assertEqual(luxury_house.garage_capacity, 4)

if __name__ == "__main__":
    unittest.main()1