"""20. Valid Parentheses (leetcode)"""

class Solution:
    """
    A class to solve the problem of Valid Parentheses.
    
    This solution uses a Stack and Hashmap approach to determine if the input string 
    has valid pairings of parentheses. Each open parenthesis is pushed onto the stack 
    and for each closing parenthesis, we check if its corresponding open parenthesis 
    is on top of the stack.

    Time complexity: O(n) - We iterate through the input string once.
    Space complexity: O(n) - In the worst case, we push all characters onto the stack.
    """
    def is_valid(self, sts: str) -> bool:
        """
        Determines if the given string has valid parentheses pairings.

        Args:
        - sts (str): The input string consisting of parentheses.

        Returns:
        - bool: True if the string has valid parentheses pairings, otherwise False.
        """
        stack = []
        close_to_open = { ")": "(", "}":"{", "]": "["}

        for c in sts:
            if c in close_to_open:
                if stack and stack[-1] == close_to_open[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False


if __name__ == "__main__":
    S = "(((()))))"
    solution = Solution()
    print("isValid:", solution.is_valid(S))
