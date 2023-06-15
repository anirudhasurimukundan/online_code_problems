import numpy as np

class Sort:
    def insertionSort(self, arr):
        for i in range(len(arr)):
            min_index = np.argmin(arr[i:]) + i
            arr[i], arr[min_index] = arr[min_index], arr[i]
        return(arr)

if __name__ == "__main__":
    sol = Sort;
    arr = [1, 4, 2, 8, 0]
    print("Sorted array = ", sol.insertionSort(sol, arr))
