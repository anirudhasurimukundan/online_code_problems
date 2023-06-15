import random

class Sort:
    def quickSort(self, arr):
        """
        Take the last element of array as pivot
        Pop that element from the array
        Assign the remainder chunk of the array into two sub arrays - array1: elements greater than pivot and array2: elements lesser than pivot
        Return the sorted array using recursion
        """
        length = len(arr)
        
        # sanity check to return single element array
        if length <= 1:
            return arr
        else:
            pivot = arr.pop()

        items_lesser = []
        items_greater = []

        for i in arr:
            if i >= pivot:
                items_greater.append(i)
            else:
                items_lesser.append(i)
        return self.quickSort(self, items_lesser) + [pivot] + self.quickSort(self, items_greater)


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
    arr = [1, 4, 2, 8, 0, 3, 4, 4]
    #arr = random.randint(0, 10, size=(1000), dtype=int)
    #print("Sorted array using insertion sort = ", sol.insertionSort(sol, arr))
    print("Sorted array using quick sort = ", sol.quickSort(sol, arr))
