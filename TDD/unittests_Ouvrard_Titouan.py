import unittest
import td2_class

class TestFastFood(unittest.TestCase):
    produit = FastFood(14.00,"S",600)

    def test_get_price(self):
        c = self.produit.get_price()
        self.assertEqual(c,14.00,"should be 14.00")

    def test_get_size(self):
        c = self.produit.get_size()
        self.assertIn(c,"S","should be S")

    def test_get_orderNumber(self):
        c = self.produit.get_orderNumber()
        self.assertEqual(c,600,"should be 600")

    burger = Burgers(14.00,"S",600)
    burger.burgersAttributes("Montagnard","Barbecue")

    def test_get_sauce(self):
        c = self.burger.get_sauce()
        self.assertEqual(c,"Barbecue", "should be Barbecue")