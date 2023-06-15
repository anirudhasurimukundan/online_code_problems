import numpy as np
"""
for i in range(n):
    min_index = np.argmin(x[i:]) + i
    x[i], x[min_index] = x[min_index], x[i]
"""
class Search:
    def linearSearch(self, arr, lookup):
        """
        This search algorithm searches through the entire array to look for the lookup number
        Time complexity: O(n)
        Space complexity: O(n)
        """
        for i in arr:
            if i == lookup:
                return(f"{lookup} found at location {i} in {arr}")
        return (f"{lookup} not found in {arr}")

    def binarySearch(self, arr, lookup):
        """
        This search algorithm divides and conquers the search process.
        Time complexity: O(logn)
        Space complexity: O(logn) with n being number of elements in array "arr"
        """
        lbound = 0
        rbound = len(arr)-1
        while lbound <= rbound:
            mid = int((lbound + rbound)*0.5)
            if lookup == arr[mid]:
                return(f"{lookup} found at location {mid} in {arr}")
            elif lookup < arr[mid]: # if lookup value is less than mid
                rbound = mid-1
            elif lookup > arr[mid]: # if lookup value is greater than mid
                lbound = mid+1
        return (f"{lookup} not found in {arr}")

if __name__ == "__main__":
    #arr = [1, 2, 4, 6, 9, 10]
    n = 1000
    arr = np.random.randint(0, 10, size=(1000), dtype=int)
    lookup = 6
    sol = Search;
    print("Binary search: ", sol.binarySearch(sol, arr, lookup))
    print("Linear search: ", sol.linearSearch(sol, arr, lookup))
