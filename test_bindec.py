import unittest
from dec2bin import decimal2binario

class TestNumeracion(unittest.TestCase):

    def test1_decimal2binario(self):
        self.assertEqual(decimal2binario(97),"01100001")

    def test2_decimal2binario(self):
        self.assertEqual(decimal2binario(52),"00110100")

    def test3_decimal2binario(self):
        self.assertEqual(decimal2binario(136),"10001000")
    
    def test4_decimal2binario(self):
        self.assertEqual(decimal2binario(89),"01011001")

if __name__ == "__main__":
    unittest.main()