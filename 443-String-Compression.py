class Solution(object):
    def compress(self, chars):
        \\\
        :type chars: List[str]
        :rtype: int
        \\\
        write = 0  # Position to write the compressed characters
        read = 0   # Position to read characters from
        
        while read < len(chars):
            char = chars[read]
            count = 0
            
            # Count the number of consecutive characters
            while read < len(chars) and chars[read] == char:
                read += 1
                count += 1
            
            # Write the character to the 'write' position
            chars[write] = char
            write += 1
            
            # If count is more than 1, write the count digits
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1
        
        return write

        