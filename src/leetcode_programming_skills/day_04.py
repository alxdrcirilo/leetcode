class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}

        for i in s:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1

        for i in t:
            if i not in d:
                return False
            else:
                if d[i] < 0:
                    return False
                d[i] -= 1

        return all(i == 0 for i in d.values())


if __name__ == "__main__":
    solution = Solution()
    assert solution.isAnagram("anagram", "nagaram")
    assert not solution.isAnagram("rat", "car")
