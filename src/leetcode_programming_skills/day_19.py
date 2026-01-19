class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:
        res = 0
        primary = [0, 0]
        secondary = [0, len(mat[0]) - 1]

        # Matrix is square
        for i in range(len(mat)):
            if primary == secondary:
                res += mat[primary[0]][primary[1]]
            else:
                res += mat[primary[0]][primary[1]]
                res += mat[secondary[0]][secondary[1]]
            primary[0] += 1
            primary[1] += 1
            secondary[0] += 1
            secondary[1] -= 1

        return res


if __name__ == "__main__":
    solution = Solution()
    assert solution.diagonalSum([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == 25
    assert (
        solution.diagonalSum(
            [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]
        )
        == 8
    )
    assert solution.diagonalSum([[5]]) == 5
