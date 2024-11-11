import unittest
from zoo import Zoo

class TestZoo(unittest.TestCase):
    def setUp(self):
        self.zoo = Zoo()

    def test_child_ticket_price_01(self):
        self.assertEqual(self.zoo.get_ticket_price(-1), "Error: Age can't be negative number.")

    def test_child_ticket_price_02(self):
        self.assertEqual(self.zoo.get_ticket_price(0), 50)
    
    def test_child_ticket_price_03(self):
        self.assertEqual(self.zoo.get_ticket_price(1), 50)
    
    def test_child_ticket_price_04(self):
        self.assertEqual(self.zoo.get_ticket_price(11), 50)
    
    def test_child_ticket_price_05(self):
        self.assertEqual(self.zoo.get_ticket_price(12), 50)
           
    def test_child_ticket_price_06(self):
        self.assertEqual(self.zoo.get_ticket_price(13), 100)
           
    def test_child_ticket_price_07(self):
        self.assertEqual(self.zoo.get_ticket_price(14), 100)
           
    def test_child_ticket_price_08(self):
        self.assertEqual(self.zoo.get_ticket_price(19), 100)
           
    def test_child_ticket_price_09(self):
        self.assertEqual(self.zoo.get_ticket_price(20), 100)
           
    def test_child_ticket_price_10(self):
        self.assertEqual(self.zoo.get_ticket_price(21), 150)
           
    def test_child_ticket_price_11(self):
        self.assertEqual(self.zoo.get_ticket_price(22), 150)
           
    def test_child_ticket_price_12(self):
        self.assertEqual(self.zoo.get_ticket_price(59), 150)
           
    def test_child_ticket_price_13(self):
        self.assertEqual(self.zoo.get_ticket_price(60), 150)
           
    def test_child_ticket_price_14(self):
        self.assertEqual(self.zoo.get_ticket_price(61), 100)
       
    # Add your additional test cases here.

if __name__ == '__main__':
    unittest.main()