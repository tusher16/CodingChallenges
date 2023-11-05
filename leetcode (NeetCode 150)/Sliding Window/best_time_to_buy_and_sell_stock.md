# [121. Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)

**Description**: Given an array `prices` where `prices[i]` is the price of a given stock on the `i`th day, find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:

- You must sell the stock before you buy again.
- You cannot sell stock on the same day you buy it.

**Example 1**:

```
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
```

**Example 2**:

```
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
```

**Constraints**:

- 1 <= prices.length <= 10^5
- 0 <= prices[i] <= 10^4

---

**Sliding Window Approach**:

The problem of maximizing profit in stock trading can be approached by using a sliding window technique. This technique involves maintaining two pointers that represent a window within the array. Here's how the approach works:

1. **Initialize Two Pointers**: Start with two pointers, `left` and `right`, initially pointing to the first and second element of the array, respectively.

2. **Iterate over the Array**: For each position in the array:
   - If the price at `right` is greater than the price at `left`, calculate the potential profit and update the maximum profit if it's higher.
   - If the price at `right` is not greater, move `left` to `right` as we found a new potential buying day.
   - Always increment `right` to explore the next selling day.

3. **Return the Maximum Profit**: After traversing the entire array, return the maximum profit.

**Python Solution**:

```python
class Solution:
    def max_profit(self, prices: list[int]) -> int:
        left, right = 0, 1
        max_pro = 0

        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                max_pro = max(max_pro, profit)
            else:
                left = right
            right += 1
        return max_pro

# Test
if __name__ == "__main__":
    PRICES = [7,1,5,3,6,4]
    solution = Solution()
    print("Max Profit:", solution.max_profit(PRICES))
```

This solution achieves a time complexity of `O(n)` where `n` is the length of the price array. The space complexity is `O(1)`, as no additional space is used beyond the input array.

## Note
Buy low and sell high. Update the buying day (`left`) when a lower price is found and calculate profit when a higher selling price (`right`) is found. Keep track of the maximum profit throughout.

---