class Solution(object):
    def minLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        while 'AB' in s or 'CD' in s:
            if 'AB' in s:
                s = s.replace('AB', '', 1)
            if 'CD' in s:
                s = s.replace('CD', '', 1)
        return len(s)