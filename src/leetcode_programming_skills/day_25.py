class Solution:
    def largestPerimeter(self, nums: list[int]) -> int:
        nums.sort(reverse=True)
        for i in range(len(nums) - 2):
            a, b, c = nums[i], nums[i + 1], nums[i + 2]
            if c + b > a:
                return a + b + c
        return 0


if __name__ == "__main__":
    solution = Solution()
    assert solution.largestPerimeter([2, 1, 2]) == 5
    assert solution.largestPerimeter([1, 2, 1, 10]) == 0
