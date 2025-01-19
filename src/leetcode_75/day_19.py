class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        right = [0]
        left = [0]

        for i in nums[::-1][:-1]:
            right.append(right[-1] + i)

        for j in range(len(nums)):
            if left[-1] - right[::-1][j] == 0:
                return j

            n = nums[j]
            left.append(left[-1] + n)

        return -1


if __name__ == "__main__":
    solution = Solution()
    test_cases = [([1, 7, 3, 6, 5, 6], 3), ([1, 2, 3], -1), ([2, 1, -1], 0)]
    for nums, expected in test_cases:
        assert solution.pivotIndex(nums) == expected
