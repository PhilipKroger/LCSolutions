class Solution(object):
    def romanToInt(self, s):
        d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        return sum([d[s[i]] for i in range(len(s))]) - (s.count('IX') * 2 + s.count('IV') * 2 + s.count('CM') * 200 + s.count('XC') * 20+ s.count('CD')*200 + s.count('XL')*20)
