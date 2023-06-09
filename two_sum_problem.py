class TwoSumSolution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        #  Naive solution
        # Looping through the whole array twice
        # Time complexity = O(n^2)
        # Memory complexity = O(n^2)
        # Logic explained:
        #   1. Loop through the whole array
        #   2. Check by brute force which two element combinations achieve target value
        #   3. If such a combination exist, then return their corresponding indices
        #   4. If no such combination exist, return a two-element list of [-1, -1]
        for i in nums:
            for j in nums:
                if i+j == target:
                    index_i = nums.index(i)
                    index_j = nums.index(j)
                    return [index_i, index_j]
        return [-1, -1] 
