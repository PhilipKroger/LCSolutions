class Solution(object):
    def countSeniors(self, details):
        """
        :type details: List[str]
        :rtype: int
        """
        k = 0
        for i in range(len(details)):
            if int(details[i][-4:-2]) > 60:
                k += 1
        return k