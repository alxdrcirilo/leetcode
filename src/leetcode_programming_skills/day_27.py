class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if a == b == "0":
            return "0"

        # Binary to decimal
        dec = 0
        for num in [a, b]:
            for n, i in enumerate(num[::-1]):
                if i == "1":
                    dec += 2**n

        # Decimal to binary
        res = []
        while dec != 0:
            q, r = dec // 2, dec % 2
            dec = q
            res.insert(0, str(r))

        return "".join(res)


if __name__ == "__main__":
    solution = Solution()
    assert solution.addBinary("11", "1") == "100"
    assert solution.addBinary("1010", "1011") == "10101"
    assert solution.addBinary("0", "0") == "0"
