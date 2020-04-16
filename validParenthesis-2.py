# Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether this
# string is valid. We define the validity of a string by these rules:

# Any left parenthesis '(' must have a corresponding right parenthesis ')'.
# Any right parenthesis ')' must have a corresponding left parenthesis '('.
# Left parenthesis '(' must go before the corresponding right parenthesis ')'.
# '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
# An empty string is also valid.
# Example 1:
# Input: "()"
# Output: True
# Example 2:
# Input: "(*)"
# Output: True
# Example 3:
# Input: "(*))"
# Output: True

# Let dp[i][j] be true if and only if the interval s[i], s[i+1], ..., s[j] can be made valid.
# Then dp[i][j] is true only if:

# s[i] is '*', and the interval s[i+1], s[i+2], ..., s[j] can be made valid;

# or, s[i] can be made to be '(', and there is some k in [i+1, j] such that s[k] can be made to be ')',
# plus the two intervals cut by s[k] (s[i+1: k] and s[k+1: j+1]) can be made valid;

class Solution(object):
    def checkValidString(self, s):
        if not s: return True
        LEFTY, RIGHTY = '(*', ')*'

        n = len(s)
        dp = [[False] * n for _ in s]
        for i in range(n):
            if s[i] == '*':
                dp[i][i] = True
            if i < n-1 and s[i] in LEFTY and s[i+1] in RIGHTY:
                dp[i][i+1] = True

        for size in range(2, n):
            for i in range(n - size):
                if s[i] == '*' and dp[i+1][i+size]:
                    dp[i][i+size] = True
                elif s[i] in LEFTY:
                    for k in range(i+1, i+size+1):
                        if (s[k] in RIGHTY and
                                (k == i+1 or dp[i+1][k-1]) and
                                (k == i+size or dp[k+1][i+size])):
                            dp[i][i+size] = True

        return dp[0][-1]

s= Solution()
print(s.checkValidString("(*()"))