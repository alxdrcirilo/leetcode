class Solution:
    def countOdds(self, low: int, high: int) -> int:
        length = high - low + 1
        count = length // 2
        return count + 1 if length % 2 and low % 2 else count


if __name__ == "__main__":
    solution = Solution()
    assert solution.countOdds(3, 7) == 3
    assert solution.countOdds(8, 10) == 1
