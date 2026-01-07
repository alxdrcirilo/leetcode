class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        return [int(i) for i in str(int("".join([str(j) for j in digits])) + 1)]


if __name__ == "__main__":
    solution = Solution()
    assert solution.plusOne([1, 2, 3]) == [1, 2, 4]
    assert solution.plusOne([9]) == [1, 0]
