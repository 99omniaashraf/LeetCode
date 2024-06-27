class Solution(object):
    def longestCommonPrefix(self, strs):
        \\\
        :type strs: List[str]
        :rtype: str
        \\\
        if not strs:
            return \\

        # Find the minimum length string from the array
        min_len = min(len(s) for s in strs)

        # Initialize the common prefix to an empty string
        common_prefix = \\

        for i in range(min_len):
            # Get the current character from the first string
            current_char = strs[0][i]

            # Check if this character is present at the same position in all strings
            if all(s[i] == current_char for s in strs):
                common_prefix += current_char
            else:
                break

        return common_prefix
        