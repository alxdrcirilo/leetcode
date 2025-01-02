class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Get smallest and longest strings
        strings = [str1, str2]
        min_chars = min(str1, str2, key=len)
        strings.remove(min_chars)
        max_chars = strings[0]

        # Store respective lengths
        min_chars_len = len(min_chars)
        max_chars_len = len(max_chars)

        # Start from largest to smallest common divisor to find gcd
        for i in range(min_chars_len, 0, -1):
            if min_chars_len % i == 0 and max_chars_len % i == 0:
                substr = min_chars[:i]
                div_rep_max = max_chars_len / len(substr)
                div_rep_min = min_chars_len / len(substr)

                # If common divisor
                if (substr * int(div_rep_max) == max_chars) and (
                    substr * int(div_rep_min) == min_chars
                ):
                    # Return gcd
                    return substr

        # No common divisor
        return ""


if __name__ == "__main__":
    solution = Solution()
    assert solution.gcdOfStrings("ABCABC", "ABC") == "ABC"
    assert solution.gcdOfStrings("ABABAB", "ABAB") == "AB"
    assert solution.gcdOfStrings("LEET", "CODE") == ""
    assert solution.gcdOfStrings("ABABABAB", "ABAB") == "ABAB"
    assert (
        solution.gcdOfStrings(
            "TAUXXTAUXXTAUXXTAUXXTAUXX", "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"
        )
        == "TAUXX"
    )
    assert solution.gcdOfStrings("AAAAAAAAA", "AAACCC") == ""
