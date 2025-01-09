class Solution:
    def compress(self, chars: list[str]) -> tuple[int, list[str]]:
        n = len(chars)
        i = 0
        idx = 0
        count = 0

        while i < n:
            c = chars[i]
            count = 0

            # Count occurences of character
            while i < n and c == chars[i]:
                i += 1
                count += 1

            # Write character to original position
            chars[idx] = c
            idx += 1

            # Write count after character if count > 1
            if count > 1:
                for digit in str(count):
                    chars[idx] = digit
                    idx += 1

        del chars[idx:]
        return idx, chars


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (["a", "a", "b", "b", "c", "c", "c"], (6, ["a", "2", "b", "2", "c", "3"])),
        (["a"], (1, ["a"])),
        (
            ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"],
            (4, ["a", "b", "1", "2"]),
        ),
    ]
    for chars, expected in test_cases:
        assert solution.compress(chars) == expected
