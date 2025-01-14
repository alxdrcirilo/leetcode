class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        a = nums[0]
        b = sum(nums[1:k])
        res = (a + b) / k

        n = len(nums)
        if n <= k:
            return sum(nums) / n

        for i in range(1, n - k + 1):
            a = nums[i]
            b -= a
            b += nums[i + k - 1]
            if (avg := (a + b) / k) > res:
                res = avg
        return res


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (([0, 1, 1, 3, 3], 4), 2.0),
        (([5], 1), 5.0),
        (([3, 3, 4, 3, 0], 3), 10 / 3),
        (([0, 1, 1, 3, 3], 4), 2.0),
    ]
    for (nums, k), expected in test_cases:
        assert solution.findMaxAverage(nums, k) == expected
