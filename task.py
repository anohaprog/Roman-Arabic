class Solution:
    def romanToInt(self, s):
        letters = [("CM", 900), ("CD", 400), ("XC", 90), ("XL", 40), ("IX", 9), ("IV", 4),
                   ("M", 1000), ("D", 500), ("C", 100), ("L", 50), ("X", 10), ("V", 5), ("I", 1)]
        result = 0
        for key, value in letters:
            result += value * s.count(key)
            s = s.replace(key, "")
        return result
