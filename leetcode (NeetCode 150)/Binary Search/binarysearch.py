"""704. Binary Search (leetcode)"""

class Solution:
    """
    A class to solve the problem of Binary Search.

    Time complexity: O(log n) - Because the algorithm divides the search space in half with each
     iteration.
    Space complexity: O(1) - No additional space is required; the search is done in place.
    """
    def search(self, nums: list[int], target: int) -> int:
        """
        Performs a binary search on an array to find a target value.

        Args:
        - nums: A list of integers where the binary search is performed.
        - target: The integer value being searched for in the list.

        Returns:
        - The index of the target if found, otherwise -1.
        """
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            guess = nums[mid]
            if guess == target:
                return mid
            elif guess < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1


if __name__ == "__main__":
    NUMS = [-1,0,3,5,9,12]
    TARGET = 9
    solution = Solution()
    print("Output:", solution.search(NUMS, TARGET))
