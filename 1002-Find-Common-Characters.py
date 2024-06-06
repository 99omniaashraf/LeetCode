class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        common_count = Counter(words[0])
        
        # Iterate through the remaining words
        for word in words[1:]:
            word_count = Counter(word)
            # Update the common_count to keep only the minimum counts
            common_count &= word_count
        
        # Expand the common characters back into a list
        result = []
        for char, count in common_count.items():
            result.extend([char] * count)
        
        return result
        