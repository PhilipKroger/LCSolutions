class Solution(object):
    def commonFactors(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        def f(n):
            l = []
            for i in range(1, n+1):
                if n%i==0:
                    l.append(i)
            return l
        return len(list(set(f(a)) & set(f(b))))