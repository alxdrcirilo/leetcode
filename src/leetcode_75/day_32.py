# Definition for singly-linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"{self.val} -> {self.next}"

    def __eq__(self, other):
        if not isinstance(other, ListNode):
            return False
        return self.val == other.val and self.next == other.next


class Solution:
    def pairSum(self, head: ListNode | None) -> int:
        ans = 0
        new_list = None
        current = head
        curent_half = head

        while curent_half and curent_half.next:
            curent_half = curent_half.next.next
            temp = current.next
            current.next = new_list
            new_list = current
            current = temp

        while current:
            ans = max(ans, current.val + new_list.val)
            current = current.next
            new_list = new_list.next

        return ans

if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (ListNode(5, ListNode(4, ListNode(2, ListNode(1)))), 6),
    ]
    for head, expected in test_cases:
        assert solution.pairSum(head) == expected

