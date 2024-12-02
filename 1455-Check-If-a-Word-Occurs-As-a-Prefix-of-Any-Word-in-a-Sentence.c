// Helper function to check if searchWord is a prefix of word
bool isPrefix(const char* word, const char* searchWord) {
    while (*searchWord) {
        if (*word != *searchWord) {
            return false;
        }
        word++;
        searchWord++;
    }
    return true;
}


int isPrefixOfWord(char* sentence, char* searchWord) {
    int wordIndex = 1; // Start with 1-indexed
    char* word = strtok(sentence, " "); // Tokenize sentence by spaces

    while (word != NULL) {
        if (isPrefix(word, searchWord)) {
            return wordIndex; // Return the 1-indexed position
        }
        word = strtok(NULL, " "); // Move to the next word
        wordIndex++;
    }

    return -1; // No match found
}