"""
for i in range(n):
    min_index = np.argmin(x[i:]) + i
    x[i], x[min_index] = x[min_index], x[i]
"""
class Search:
    def binarySearch(self, arr, lookup):
        """
        This search algorithm divides and conquers the search process.
        Time complexity: O(logn)
        Space complexity: O(n) with n being number of elements in array "arr"
        """
        lbound = 0
        rbound = len(arr)-1
        i = 0
        while lbound < rbound:
            mid = int((lbound + rbound)*0.5)
            if lookup == arr[mid]:
                return("Found at location ", ind)
            elif lookup < arr[mid]: # if lookup value is less than mid
                rbound = mid-1
            elif lookup > arr[mid]:
                lbound = mid+1
        return (f"{lookup} not found in {arr}")

if __name__ == "__main__":
    arr = [1, 2, 4, 6, 9, 10]
    lookup = 7
    sol = Search;
    print(sol.binarySearch(sol, arr, lookup))
