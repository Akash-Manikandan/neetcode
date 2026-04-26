class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def dp(curr):
            if curr == n:
                return 1

            if curr > n:
                return 0

            if curr in memo:
                return memo[curr]

            memo[curr] = dp(curr + 1) + dp(curr + 2)

            return memo[curr]

        return dp(0)
