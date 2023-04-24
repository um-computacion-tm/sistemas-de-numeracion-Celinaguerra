import unittest
from dec2binocthex import decimal2binario
from dec2binocthex import decimal2octal
from dec2binocthex import decimal2hexadecimal

from binocthex2dec import binario2decimal
from binocthex2dec import octal2decimal
from binocthex2dec import hexadecimal2decimal

from bin2octhex import binario2octal
from bin2octhex import binario2hexadecimal

from octhex2bin import octal2binario
from octhex2bin import hexadecimal2binario

from oct2hex import octal2hexadecimal

from hex2oct import hexadecimal2octal

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

    def test1_octal2decimal(self):
        self.assertEqual(octal2decimal(15),"13")

    def test2_octal2decimal(self):
        self.assertEqual(octal2decimal(304),"196")

    def test3_octal2decimal(self):
        self.assertEqual(octal2decimal(372),"250")

    def test4_octal2decimal(self):
        self.assertEqual(octal2decimal(251),"169")

###################################################################

    def test1_hexadecimal2decimal(self):
        self.assertEqual(hexadecimal2decimal("D"),"13")

    def test2_hexadecimal2decimal(self):
        self.assertEqual(hexadecimal2decimal("C4"),"196")

    def test3_hexadecimal2decimal(self):
        self.assertEqual(hexadecimal2decimal("FA"),"250")

    def test4_hexadecimal2decimal(self):
        self.assertEqual(hexadecimal2decimal("A9"),"169")

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

###################################################################

    def test1_octal2binario(self):
        self.assertEqual(octal2binario("23"),"010011")

    def test2_octal2binario(self):
        self.assertEqual(octal2binario("35"),"011101")

    def test3_octal2binario(self):
        self.assertEqual(octal2binario("123"),"001010011")

    def test4_octal2binario(self):
        self.assertEqual(octal2binario("71"),"111001")

#####################################################################

    def test1_hexadecimal2binario(self):
        self.assertEqual(hexadecimal2binario("B5"),"10110101")

    def test2_hexadecimal2binario(self):
        self.assertEqual(hexadecimal2binario("D1"),"11010001")

    def test3_hexadecimal2binario(self):
        self.assertEqual(hexadecimal2binario("FB"),"11111011")

    def test4_hexadecimal2binario(self):
        self.assertEqual(hexadecimal2binario("9C"),"10011100")

#####################################################################

    def test1_octal2hexadecimal(self):
        self.assertEqual(octal2hexadecimal("23"),"13")

    def test2_octal2hexadecimal(self):
        self.assertEqual(octal2hexadecimal("35"),"1D")

    def test3_octal2hexadecimal(self):
        self.assertEqual(octal2hexadecimal("123"),"53")

    def test4_octal2hexadecimal(self):
        self.assertEqual(octal2hexadecimal("71"),"39")

#####################################################################

    def test1_hexadecimal2octal(self):
        self.assertEqual(hexadecimal2octal("CD"),"315")

    def test2_hexadecimal2octal(self):
        self.assertEqual(hexadecimal2octal("B9"),"271")

    def test3_hexadecimal2octal(self):
        self.assertEqual(hexadecimal2octal("D12"),"6422")

    def test4_hexadecimal2octal(self):
        self.assertEqual(hexadecimal2octal("1A"),"32")


if __name__ == "__main__":
    unittest.main()
