class Solution(object):
    def longestPalindrome(self, s):
        \\\
        :type s: str
        :rtype: int
        \\\
        char_freq = {}
        for char in s:
            char_freq[char] = char_freq.get(char, 0) + 1

        palindrome_length = 0
        has_odd_freq = False
        for freq in char_freq.values():
            palindrome_length += freq // 2 * 2
            if freq % 2 == 1:
                has_odd_freq = True
        
        if has_odd_freq:
            palindrome_length += 1
        
        return palindrome_length
        