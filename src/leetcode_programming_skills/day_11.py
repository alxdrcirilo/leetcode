class Solution:
    def romanToInt(self, s: str) -> int:
        roman_nums = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        substract = {
            "IV": "IIII",
            "IX": "VIIII",
            "XL": "XXXX",
            "XC": "LXXXX",
            "CD": "CCCC",
            "CM": "DCCCC",
        }

        for k, v in substract.items():
            s = s.replace(k, v)

        return sum(roman_nums[c] for c in s)


if __name__ == "__main__":
    solution = Solution()
    assert solution.romanToInt("III") == 3
    assert solution.romanToInt("LVIII") == 58
    assert solution.romanToInt("MCMXCIV") == 1994
