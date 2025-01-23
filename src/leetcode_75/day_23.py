class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        n = len(grid)
        columns = [[grid[row][col] for row in range(n)] for col in range(n)]

        count = 0
        for r in grid:
            for c in columns:
                if r == c:
                    count += 1
        return count


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        ([[3, 2, 1], [1, 7, 6], [2, 7, 7]], 1),
        ([[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]], 3),
    ]
    for grid, expected in test_cases:
        assert solution.equalPairs(grid) == expected
