class Solution(object):
    def replaceWords(self, dictionary, sentence):
        \\\
        :type dictionary: List[str]
        :type sentence: str
        :rtype: str
        \\\
        # Create a set for faster lookup
        root_set = set(dictionary)
        
        # Function to find the root for a given word
        def find_root(word):
            for i in range(1, len(word) + 1):
                if word[:i] in root_set:
                    return word[:i]
            return word
        
        # Split the sentence into words
        words = sentence.split()
        
        # Replace each word with its root
        result = [find_root(word) for word in words]
        
        # Join the words back into a sentence
        return ' '.join(result)