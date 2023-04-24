import unittest
from dec2binocthex import decimal2binario
from dec2binocthex import decimal2octal
from dec2binocthex import decimal2hexadecimal

from bin2dec import binario2decimal
from bin2dec import binario2octal
from bin2dec import binario2hexadecimal

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

    def test1_binario2octal(self):
        self.assertEqual(binario2octal(1101),"15")

    def test2_binario2octal(self):
        self.assertEqual(binario2octal(11000100),"304")

    def test3_binario2octal(self):
        self.assertEqual(binario2octal(11111010),"372")

    def test4_binario2octal(self):
        self.assertEqual(binario2octal(10101001),"251")

###################################################################

    def test1_binario2hexadecimal(self):
        self.assertEqual(binario2hexadecimal(1101),"D")

    def test2_binario2hexadecimal(self):
        self.assertEqual(binario2hexadecimal(11000100),"C4")

    def test3_binario2hexadecimal(self):
        self.assertEqual(binario2hexadecimal(11111010),"FA")

    def test4_binario2hexadecimal(self):
        self.assertEqual(binario2hexadecimal(10101001),"A9")


if __name__ == "__main__":
    unittest.main()