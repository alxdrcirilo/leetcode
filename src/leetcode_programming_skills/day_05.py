class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        if n < 2:
            return False

        if len(set(s)) == 1:
            return True

        div = 2
        while div <= n // 2:
            if not n % div:
                if s[: n // div] * div == s:
                    return True
            div += 1
        return False


if __name__ == "__main__":
    solution = Solution()
    assert solution.repeatedSubstringPattern("abab")
    assert not solution.repeatedSubstringPattern("aba")
    assert solution.repeatedSubstringPattern("abcabcabcabc")
    assert not solution.repeatedSubstringPattern("abac")
    assert solution.repeatedSubstringPattern("ababab")
    assert solution.repeatedSubstringPattern("ababababab")
    assert solution.repeatedSubstringPattern("bb")
    assert solution.repeatedSubstringPattern("zzz")
    assert solution.repeatedSubstringPattern("babbabbabbabbab")
