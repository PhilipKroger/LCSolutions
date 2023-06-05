class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = ''.join(i for i in s if i.isalpha() or i.isdigit())
        s = s.lower()
        s1 = s[:][::-1]
        if s==s1:
            return True
        else: return False
