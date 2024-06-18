class Solution(object):
    def judgeSquareSum(self, c):
        \\\
        :type c: int
        :rtype: bool
        \\\
        a = 0
        b = int(math.sqrt(c))
        
        while a <= b:
            current_sum = a * a + b * b
            if current_sum == c:
                return True
            elif current_sum < c:
                a += 1
            else:
                b -= 1
        
        return False
        