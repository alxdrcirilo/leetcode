class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        return max([sum(i) for i in accounts])


if __name__ == "__main__":
    solution = Solution()
    assert solution.maximumWealth([[1, 2, 3], [3, 2, 1]]) == 6
    assert solution.maximumWealth([[1, 5], [7, 3], [3, 5]]) == 10
    assert solution.maximumWealth([[2, 8, 7], [7, 1, 3], [1, 9, 5]]) == 17
