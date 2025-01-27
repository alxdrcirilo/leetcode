class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        current = ""
        d = 0

        for char in s:
            if char.isdigit():
                # Build the number for repeat count
                d = d * 10 + int(char)
            elif char == "[":
                # Push the current context to stack
                stack.append((current, d))
                current = ""
                d = 0
            elif char == "]":
                # Pop and combine the repeated substring
                prev, repeat = stack.pop()
                current = prev + current * repeat
            else:
                # Append character to the current string
                current += char

        return current


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        ("3[a]2[bc]", "aaabcbc"),
        ("3[a2[c]]", "accaccacc"),
        ("2[abc]3[cd]ef", "abcabccdcdcdef"),
    ]
    for s, expected in test_cases:
        assert solution.decodeString(s) == expected
