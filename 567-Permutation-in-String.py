from collections import Counter

class Solution(object):
    def checkInclusion(self, s1, s2):
        \\\
        :type s1: str
        :type s2: str
        :rtype: bool
        \\\
        len1, len2 = len(s1), len(s2)
        
        if len1 > len2:
            return False
        
        # Frequency counter for s1
        s1_count = Counter(s1)
        
        # Frequency counter for the current window in s2
        window_count = Counter(s2[:len1])
        
        if s1_count == window_count:
            return True
        
        # Sliding the window
        for i in range(len1, len2):
            # Include the new character in the window
            window_count[s2[i]] += 1
            # Remove the oldest character from the window
            window_count[s2[i - len1]] -= 1
            
            # Remove the count entry if it drops to zero
            if window_count[s2[i - len1]] == 0:
                del window_count[s2[i - len1]]
            
            # Compare counts
            if s1_count == window_count:
                return True
        
        return False
