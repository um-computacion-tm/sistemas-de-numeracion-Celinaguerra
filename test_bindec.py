import unittest
from dec2bin import decimal2binario
from bin2dec import binario2decimal

class TestNumeracion(unittest.TestCase):

    def test1_decimal2binario(self):
        self.assertEqual(decimal2binario(97),"01100001")

    def test2_decimal2binario(self):
        self.assertEqual(decimal2binario(52),"00110100")

    def test3_decimal2binario(self):
        self.assertEqual(decimal2binario(136),"10001000")
    
    def test4_decimal2binario(self):
        self.assertEqual(decimal2binario(89),"01011001")

    def test1_binario2decimal(self):
        self.assertEqual(binario2decimal(1101),"13")

    def test2_binario2decimal(self):
        self.assertEqual(binario2decimal(11000100),"196")

    def test3_binario2decimal(self):
        self.assertEqual(binario2decimal(11111010),"250")

    def test4_binario2decimal(self):
        self.assertEqual(binario2decimal(10101001),"169")

if __name__ == "__main__":
    unittest.main()