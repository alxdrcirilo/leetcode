class Solution:
    def reverseVowels(self, s: str) -> str:
        string = list(s)
        vowels = set("aAeEiIoOuU")

        # Two pointers
        left, right = 0, len(string) - 1
        while left < right:
            a, b = string[left], string[right]
            if a not in vowels:
                left += 1
            elif b not in vowels:
                right -= 1
            else:
                string[left], string[right] = b, a
                left += 1
                right -= 1

        return "".join(string)


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        ("IceCreAm", "AceCreIm"),
        ("leetcode", "leotcede"),
        ("AirpOrt", "OirpArt"),
    ]

    for s, expected in test_cases:
        assert solution.reverseVowels(s) == expected
