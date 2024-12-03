char* addSpaces(char* s, int* spaces, int spacesSize) {
    int sLength = strlen(s);
    // Calculate the length of the new string
    int newLength = sLength + spacesSize;

    // Allocate memory for the new string (+1 for the null terminator)
    char* result = (char*)malloc((newLength + 1) * sizeof(char));
    if (!result) return NULL; // Check for memory allocation failure

    int i = 0, j = 0, k = 0;
    while (i < sLength) {
        // If the current index matches a space position, add a space
        if (k < spacesSize && i == spaces[k]) {
            result[j++] = ' ';
            k++;
        }
        // Copy the character from the original string
        result[j++] = s[i++];
    }

    // Null-terminate the new string
    result[newLength] = '\0';

    return result;
}

