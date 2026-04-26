from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        def rob1(house: List[int]) -> int:
            memo = {}

            def dp(n: int) -> int:
                if n in memo:
                    return memo[n]

                if n >= len(house):
                    return 0

                memo[n] = max(house[n] + dp(n + 2), dp(n + 1))
                return memo[n]

            return dp(0)

        return max(rob1(nums[1:]), rob1(nums[:-1]))
