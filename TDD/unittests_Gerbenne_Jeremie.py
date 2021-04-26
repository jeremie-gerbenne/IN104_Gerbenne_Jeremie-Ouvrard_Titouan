import unittest
import td2_class

class TestFastFood(unittest.TestCase):
    produit = FastFood(10.95,"XL",521)

    def test_get_orderNumber(self):
        c = self.produit.get_orderNumber()
        self.assertEqual(c,521,"should be 521")

    def test_getsize(self):
        c = self.produit.get_size()
        self.assertIn(c,["S","M","L","XL"],"should be S, M, L or XL")

    def test_getprice(self):
        c = self.produit.get_price()
        self.assertEqual(c,10.95,"should be 10.95€")

    tacos = Tacos(10.95,"XL",521)
    tacos.tacosAttributes("cordon bleu","ketchup")

    def test_get_ingredient(self):
        liste = self.tacos.get_ingredient()
        self.assertEqual(liste, ["cordon bleu","ketchup"], "should be cordon bleu ketchup")


