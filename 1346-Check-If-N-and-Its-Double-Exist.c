bool checkIfExist(int* arr, int arrSize) {
    // Iterate through each pair of elements in the array
    for (int i = 0; i < arrSize; i++) {
        for (int j = 0; j < arrSize; j++) {
            // Check if arr[i] is double of arr[j] and i != j
            if (i != j && arr[i] == 2 * arr[j]) {
                return true;
            }
        }
    }
    return false; // Return false if no such pair is found
}
