import numpy as np

class Sort:
    def insertionSort(self, arr):
        """
        Find the smallest element of the remaining chunk of the array
        Swap the current element with the smallest element in the remainder chunk of the array
        Time complexity: O(n^2)
        Memory complexity: O(n)
        """
        for i in range(len(arr)):
            min_index = np.argmin(arr[i:]) + i
            arr[i], arr[min_index] = arr[min_index], arr[i]
        return(arr)

if __name__ == "__main__":
    sol = Sort;
    #arr = [1, 4, 2, 8, 0]
    arr = np.random.randint(0, 10, size=(1000), dtype=int)
    print("Sorted array = ", sol.insertionSort(sol, arr))
