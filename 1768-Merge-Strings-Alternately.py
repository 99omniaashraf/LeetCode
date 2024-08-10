class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        result = []
        i, j = 0, 0
        len1, len2 = len(word1), len(word2)
        
        # Merge characters alternately
        while i < len1 and j < len2:
            result.append(word1[i])
            result.append(word2[j])
            i += 1
            j += 1
        
        # Append remaining characters if any
        while i < len1:
            result.append(word1[i])
            i += 1
        
        while j < len2:
            result.append(word2[j])
            j += 1
        
        # Join the list into a single string and return it
        return ''.join(result)
        