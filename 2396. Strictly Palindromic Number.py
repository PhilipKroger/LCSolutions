class Solution(object):
    def isStrictlyPalindromic(self, n):
        """
        :type n: int
        :rtype: bool
        """
        lst = []
        for i in range(2, n-1):
            w_palendrom = ''
            new_n = n
            while new_n > 0:
                w_palendrom += str(new_n%i)
                new_n = new_n//i
            lst.append(w_palendrom)
        count = 0
        for i in range(len(lst)):
            count1 = lst[i]
            if count1 == count1[::-1]:
                count += 1
        if count == len(lst):
            return True
        else:
            return False
