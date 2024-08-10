class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        # Check if str1 + str2 is the same as str2 + str1
        if str1 + str2 != str2 + str1:
            return ""
        
        # Compute the GCD of lengths of str1 and str2
        gcd_length = gcd(len(str1), len(str2))
        
        # The potential GCD string is the substring of length gcd_length from str1
        gcd_string = str1[:gcd_length]
        
        # Verify if gcd_string can form both str1 and str2 by repeating
        if str1 == gcd_string * (len(str1) // gcd_length) and str2 == gcd_string * (len(str2) // gcd_length):
            return gcd_string
        
        return ""
