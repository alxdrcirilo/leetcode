class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> list[list[int]]:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = set()
        cols = set()

        # m * n matrix
        m = len(matrix)
        n = len(matrix[0])

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)

        for i in rows:
            matrix[i] = [0] * n
        for j in cols:
            for i in range(m):
                matrix[i][j] = 0

        return matrix


if __name__ == "__main__":
    solution = Solution()
    assert solution.setZeroes([[1, 1, 1], [1, 0, 1], [1, 1, 1]]) == [
        [1, 0, 1],
        [0, 0, 0],
        [1, 0, 1],
    ]
    assert solution.setZeroes([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]) == [
        [0, 0, 0, 0],
        [0, 4, 5, 0],
        [0, 3, 1, 0],
    ]
