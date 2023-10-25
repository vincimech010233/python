"""
Write two functions that convert a roman numeral to and from an integer value. Multiple roman numeral values will be tested for each function.

Modern Roman numerals are written by expressing each digit separately starting with the left most digit and skipping any digit with a value of zero. In Roman numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC. 2008 is written as 2000=MM, 8=VIII; or MMVIII. 1666 uses each Roman symbol in descending order: MDCLXVI.

Input range : 1 <= n < 4000

In this kata 4 should be represented as IV, NOT as IIII (the "watchmaker's four").

Examples
to roman:
2000 -> "MM"
1666 -> "MDCLXVI"
1000 -> "M"
 400 -> "CD"
  90 -> "XC"
  40 -> "XL"
   1 -> "I"

from roman:
"MM"      -> 2000
"MDCLXVI" -> 1666
"M"       -> 1000
"CD"      -> 400
"XC"      -> 90
"XL"      -> 40
"I"       -> 1

Help
Symbol	Value
I	1
IV	4
V	5
X	10
L	50
C	100
D	500
M	1000
"""

class RomanNumerals:
    @staticmethod
    def to_roman(value):
        val_to_roman = {
            1000: 'M', 900: 'CM', 500: 'D', 400: 'CD',
            100: 'C', 90: 'XC', 50: 'L', 40: 'XL',
            10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'
        }
        roman_numeral = ''
        for roman_value, numeral in val_to_roman.items():
            while value >= roman_value:
                roman_numeral += numeral
                value -= roman_value
        return roman_numeral
    
    @staticmethod
    def from_roman(roman_numeral):
        roman_to_val = {
            'M': 1000, 'CM': 900, 'D': 500, 'CD': 400,
            'C': 100, 'XC': 90, 'L': 50, 'XL': 40,
            'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1
        }
        num = 0
        prev_value = None
        
        for numeral in reversed(roman_numeral):
            value = roman_to_val[numeral]
            if prev_value is None or value >= prev_value:
                num += value
            else:
                num -= value
            prev_value = value
        
        return num

if __name__ == '__main__':
    print(RomanNumerals.to_roman(1990))
    print(RomanNumerals.from_roman('MCMXC'))
    print(RomanNumerals.from_roman('MM'))

