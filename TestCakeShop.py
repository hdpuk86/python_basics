import unittest
from CakeShop import CakeShop
from Cake import Cake

class TestCakeShop(unittest.TestCase):
    def setUp(self):
        brownie_ingredients = ["chocolate", "butter", "eggs", "flour", "sugar"]
        self.cake1 = Cake("brownie", brownie_ingredients, 3)
        sponge_ingredients = ["flour", "sugar", "eggs", "butter"]
        self.cake2 = Cake("sponge", sponge_ingredients, 3)
        carrot_cake_ingredients = ["carrot", "flour", "eggs"]
        self.cake3 = Cake("carrot cake", carrot_cake_ingredients, 3)
        cakes = [self.cake1, self.cake2, self.cake3]
        self.cakeshop = CakeShop("Cakey", cakes)

    def test_cakeshop_name(self):
        self.assertEquals("Cakey", self.cakeshop.name)

    def test_cakeshop_has_cakes(self):
        self.assertEquals(3, len(self.cakeshop.cakes))

    def test_cakeshop_average_rating(self):
        self.assertEquals(3, self.cakeshop.average_rating())

unittest.main()
