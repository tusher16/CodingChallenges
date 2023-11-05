"""121. Best Time to Buy and Sell Stock (leetcode)"""

class Solution:
    """
    A class to solve the problem of finding the maximum profit from a list of stock prices.
    This solution uses a sliding window approach to find the maximum profit.
    Time complexity: O(n), where n is the length of the price list.
    Space complexity: O(1), as no additional space is used.
    """
    def max_profit(self, prices: list[int]) -> int:
        """
        Calculates the maximum profit that can be achieved from a single transaction.

        Args:
        - prices (list[int]): A list of stock prices where prices[i] 
        is the price of a given stock on the ith day.

        Returns:
        - int: The maximum profit that can be achieved from a single buy and sell transaction.
        """
        left, right = 0, 1
        max_pro = 0

        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                max_pro = max(max_pro, profit)
            else:
                left = right    # Move the left pointer to the right if we found a lower price
            right += 1          # Always move the right pointer to explore further
        return max_pro

if __name__ == "__main__":
    PRICES = [7,1,5,3,6,4]
    solution = Solution()
    print("Max Profit:", solution.max_profit(PRICES))
