class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        for i in range(len(s.split(' '))-1, -1, -1):
            s.split(' ')[i] = s.split(' ')[i][::-1]
        return ' '.join(s.split(' '))