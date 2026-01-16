class Solution:
    def tictactoe(self, moves: list[list[int]]) -> str:
        """
        Possible winning combinations:
            - Rows: 0, 1, 2
            - Columns: 3, 4, 5
            - Diagonal: 6 (top-left to bottom-right)
            - Anti-diagonal: 7 (top-right to bottom-left)
        """

        a = [0] * 8
        b = [0] * 8

        for i, (row, col) in enumerate(moves):
            player = a if i % 2 == 0 else b
            player[row] += 1
            player[col + 3] += 1
            if row == col:
                player[6] += 1
            if row == 2 - col:
                player[7] += 1

        for i in range(8):
            if a[i] == 3:
                return "A"
            if b[i] == 3:
                return "B"

        return "Draw" if len(moves) == 9 else "Pending"


if __name__ == "__main__":
    solution = Solution()
    assert solution.tictactoe([[0, 0], [2, 0], [1, 1], [2, 1], [2, 2]]) == "A"
    assert (
        solution.tictactoe([[0, 0], [1, 1], [0, 1], [0, 2], [1, 0], [2, 0]])
        == "B"
    )
    assert (
        solution.tictactoe(
            [
                [0, 0],
                [1, 1],
                [2, 0],
                [1, 0],
                [1, 2],
                [2, 1],
                [0, 1],
                [0, 2],
                [2, 2],
            ]
        )
        == "Draw"
    )
    assert solution.tictactoe([[0, 0], [1, 1]]) == "Pending"
    assert (
        solution.tictactoe([[1, 0], [2, 2], [2, 0], [0, 1], [1, 1]])
        == "Pending"
    )
