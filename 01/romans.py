# Arquivo: romans.py

def int_to_roman(num):
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
        ]
    syb = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
        ]
    roman_num = ''
    i = 0
    while num > 0:
        for _ in range(num // val[i]):
            roman_num += syb[i]
            num -= val[i]
        i += 1
    return roman_num

def roman_to_int(s):
    roman = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000,
        'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90,
        'CD': 400, 'CM': 900
    }
    i = 0
    num = 0
    while i < len(s):
        if i+1 < len(s) and s[i:i+2] in roman:
            num += roman[s[i:i+2]]
            i += 2
        else:
            num += roman[s[i]]
            i += 1
    return num
# Arquivo: test_romans.py

import unittest
from romans import int_to_roman, roman_to_int

class TestRomans(unittest.TestCase):

    def test_single_digits(self):
        self.assertEqual(int_to_roman(1), "I")
        self.assertEqual(int_to_roman(3), "III")
        self.assertEqual(int_to_roman(4), "IV")
        self.assertEqual(int_to_roman(9), "IX")

    def test_double_digits(self):
        self.assertEqual(int_to_roman(10), "X")
        self.assertEqual(int_to_roman(23), "XXIII")
        self.assertEqual(int_to_roman(49), "XLIX")
        self.assertEqual(int_to_roman(58), "LVIII")

    def test_hundred_values(self):
        self.assertEqual(int_to_roman(100), "C")
        self.assertEqual(int_to_roman(399), "CCCXCIX")
        self.assertEqual(int_to_roman(444), "CDXLIV")
        self.assertEqual(int_to_roman(500), "D")

    def test_thousand_values(self):
        self.assertEqual(int_to_roman(1000), "M")
        self.assertEqual(int_to_roman(1984), "MCMLXXXIV")
        self.assertEqual(int_to_roman(2021), "MMXXI")
        self.assertEqual(int_to_roman(3999), "MMMCMXCIX")

    def test_edge_cases(self):
        self.assertEqual(int_to_roman(1), "I")
        self.assertEqual(int_to_roman(3999), "MMMCMXCIX")

    def test_single_digits_roman_to_int(self):
        self.assertEqual(roman_to_int("I"), 1)
        self.assertEqual(roman_to_int("III"), 3)
        self.assertEqual(roman_to_int("IV"), 4)
        self.assertEqual(roman_to_int("IX"), 9)

    def test_double_digits_roman_to_int(self):
        self.assertEqual(roman_to_int("X"), 10)
        self.assertEqual(roman_to_int("XXIII"), 23)
        self.assertEqual(roman_to_int("XLIX"), 49)
        self.assertEqual(roman_to_int("LVIII"), 58)

    def test_hundred_values_roman_to_int(self):
        self.assertEqual(roman_to_int("C"), 100)
        self.assertEqual(roman_to_int("CCCXCIX"), 399)
        self.assertEqual(roman_to_int("CDXLIV"), 444)
        self.assertEqual(roman_to_int("D"), 500)

    def test_thousand_values_roman_to_int(self):
        self.assertEqual(roman_to_int("M"), 1000)
        self.assertEqual(roman_to_int("MCMLXXXIV"), 1984)
        self.assertEqual(roman_to_int("MMXXI"), 2021)
        self.assertEqual(roman_to_int("MMMCMXCIX"), 3999)

    def test_edge_cases_roman_to_int(self):
        self.assertEqual(roman_to_int("I"), 1)
        self.assertEqual(roman_to_int("MMMCMXCIX"), 3999)

if __name__ == "__main__":
    unittest.main()
