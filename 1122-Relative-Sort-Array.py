class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        # Create a dictionary to store the indices of elements in arr2
        indices = {num: i for i, num in enumerate(arr2)}

        # Define a custom sorting key function
        def key_func(num):
            if num in indices:
                # For elements in arr2, return their corresponding index
                return indices[num]
            else:
                # For elements not in arr2, return a tuple with a large number and the element itself
                return (float('inf'), num)

        # Sort arr1 using the custom key function
        arr1.sort(key=key_func)

        return arr1