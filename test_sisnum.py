import unittest
from dec2binocthex import decimal2binario
from dec2binocthex import decimal2octal
from dec2binocthex import decimal2hexadecimal

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

#################################################################

    def test1_decimal2octal(self):
        self.assertEqual(decimal2octal(97),"141")

    def test2_decimal2octal(self):
        self.assertEqual(decimal2octal(52),"64")

    def test3_decimal2octal(self):
        self.assertEqual(decimal2octal(136),"210")
    
    def test4_decimal2octal(self):
        self.assertEqual(decimal2octal(89),"131")

###################################################################

    def test1_decimal2hexadecimal(self):
        self.assertEqual(decimal2hexadecimal(97),"61")

    def test2_decimal2hexadecimal(self):
        self.assertEqual(decimal2hexadecimal(52),"34")

    def test3_decimal2hexadecimal(self):
        self.assertEqual(decimal2hexadecimal(136),"88")
    
    def test4_decimal2hexadecimal(self):
        self.assertEqual(decimal2hexadecimal(89),"59")

###################################################################

    def test1_binario2decimal(self):
        self.assertEqual(binario2decimal(1101),"13")

    def test2_binario2decimal(self):
        self.assertEqual(binario2decimal(11000100),"196")

    def test3_binario2decimal(self):
        self.assertEqual(binario2decimal(11111010),"250")

    def test4_binario2decimal(self):
        self.assertEqual(binario2decimal(10101001),"169")

###################################################################

if __name__ == "__main__":
    unittest.main()