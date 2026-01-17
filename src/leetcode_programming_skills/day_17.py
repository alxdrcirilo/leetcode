class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        direction = (0, 1)  # North
        position = [0, 0]

        for i in instructions:
            match i:
                case "G":
                    position = [a + b for (a, b) in zip(position, direction)]
                case "L":
                    direction = (-direction[1], direction[0])
                case "R":
                    direction = (direction[1], -direction[0])

        return position == [0, 0] or direction != (0, 1)


if __name__ == "__main__":
    solution = Solution()
    assert solution.isRobotBounded("GGLLGG")
    assert not solution.isRobotBounded("GG")
    assert solution.isRobotBounded("GL")
    assert solution.isRobotBounded("GLRLLGLL")
