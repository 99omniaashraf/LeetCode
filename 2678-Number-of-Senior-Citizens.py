class Solution(object):
    def countSeniors(self, details):
        """
        :type details: List[str]
        :rtype: int
        """
        count = 0

        for detail in details:
            age_str = detail[11:13]
            age = int(age_str)

            if age > 60:
                count += 1
        return count