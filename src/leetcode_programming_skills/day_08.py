class Solution:
    def arraySign(self, nums: list[int]) -> int:
        count_neg = 0
        for i in nums:
            if i == 0:
                return 0
            count_neg += 1 if i < 0 else 0
        return -1 if count_neg % 2 else 1


if __name__ == "__main__":
    solution = Solution()
    assert solution.arraySign([-1, -2, -3, -4, 3, 2, 1]) == 1
    assert solution.arraySign([1, 5, 0, 2, -3]) == 0
    assert solution.arraySign([-1, 1, -1, 1, -1]) == -1
