import unittest
from item import Item
from shopping_basket import Basket



class ShopingBasketTest(unittest.TestCase):
    def test_empty_basket_total(self):
        basket = Basket([])
        self.assertEqual(basket.total(), 0)

    def test_single_item_quantity(self):
        basket = Basket([Item(100.0, 1)])
        self.assertEqual(basket.total(), 100.0)

    def test_two_items_quantity_one(self):
        basket = Basket([Item(100.0, 1), Item(100.0, 1)])
        self.assertEqual(basket.total(), 200.0)


    def test_single_item_quantity_two(self):
        basket = Basket([Item(100.0, 2)])
        self.assertEqual(basket.total(), 200.0)



if __name__ == "__main__":
    pass