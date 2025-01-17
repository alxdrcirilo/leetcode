class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        if sum(nums) == 0:
            return 0

        a = 0
        b = 0
        zeros = 0
        res = 0

        for i in range(len(nums)):
            n = nums[i]
            if n == 0:
                if zeros == 0:
                    zeros += 1
                    b += 1
                elif zeros == 1:
                    while zeros == 1:
                        zeros -= 1 if nums[a] == 0 else 0
                        a += 1
                    zeros = 1
                    b += 1
            elif n == 1:
                b += 1
            if (c := b - 1 - a) > res:
                res = c
        return res


if __name__ == "__main__":
    solution = Solution()
    test_cases = [([1, 1, 0, 1], 3), ([0, 1, 1, 1, 0, 1, 1, 0, 1], 5), ([1, 1, 1], 2)]
    for nums, expected in test_cases:
        assert solution.longestSubarray(nums) == expected
