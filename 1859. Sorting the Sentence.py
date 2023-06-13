class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.split()
        for i in range(len(s)-1):
            for j in range(len(s)-i-1):
                if int(s[j+1][-1]) < int(s[j][-1]):
                    s[j], s[j+1] = s[j+1], s[j]
        for i in range(len(s)):
            s[i] = s[i][:-1]
        s = ' '.join(s)
        return s
