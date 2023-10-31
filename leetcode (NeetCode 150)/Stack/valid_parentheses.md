# [20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)

**Description**: Given a string `s` containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

**Example 1**:

```
Input: s = "()"
Output: true
```

**Example 2**:

```
Input: s = "()[]{}"
Output: true
```

**Example 3**:

```
Input: s = "(]"
Output: false
```

**Constraints**:

- 1 <= s.length <= 10^4
- s consists of parentheses only '()[]{}'.

---

**Stack and HashMap Approach**:

The problem of validating parentheses can be efficiently solved using a stack. A stack is a Last-In-First-Out (LIFO) data structure, making it ideal for this kind of problem where we need to ensure that the most recent open parenthesis is closed first. Here's how the approach works:

1. **Initialize a Stack**: Use a stack to keep track of the open parentheses.

2. **Use a HashMap**: A dictionary is used to map closing parentheses to their corresponding opening parentheses. This makes it easy to check if the current character is a closing parenthesis and, if so, what its corresponding opening parenthesis is.

3. **Iterate over the String**: For each character in the string:
   - If it's an opening parenthesis, push it onto the stack.
   - If it's a closing parenthesis:
     - Check if the stack is empty (meaning there's no matching open parenthesis). If it's empty, the string is not valid.
     - Check if the top of the stack has the corresponding opening parenthesis for the current closing parenthesis. If not, the string is not valid.
     - Pop the top of the stack.

4. **Check the Stack at the End**: After processing all characters, if the stack is not empty, it means there are unmatched opening parentheses, and the string is not valid. If it's empty, the string is valid.

**Python Solution**:

```python
class Solution:
    def is_valid(self, s: str) -> bool:
        stack = []
        close_to_open = { ")": "(", "}": "{", "]": "[" }

        for c in s:
            if c in close_to_open:
                if stack and stack[-1] == close_to_open[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return not stack

# Test
S = "([)]"
solution = Solution()
print("isValid:", solution.is_valid(S))
```

This solution achieves a time complexity of `O(n)` where `n` is the length of the string. The space complexity is also `O(n)`, which corresponds to the space needed for the stack in the worst-case scenario where all characters are opening parentheses.

## Note
Push open braces onto the stack, pop when there's a matching close brace, and if the stack is empty at the end, the parentheses are valid.