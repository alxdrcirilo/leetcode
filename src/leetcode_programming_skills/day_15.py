class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x = y = 0
        for i in moves:
            match i:
                case "U":
                    y += 1
                case "D":
                    y -= 1
                case "R":
                    x += 1
                case "L":
                    x -= 1
        return x == 0 and y == 0


if __name__ == "__main__":
    solution = Solution()
    assert solution.judgeCircle("UD") is True
    assert solution.judgeCircle("LL") is False
