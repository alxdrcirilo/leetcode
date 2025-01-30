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
    def deleteMiddle(self, head: ListNode | None) -> ListNode | None:
        if head is None:
            return None

        prev = ListNode(0)
        prev.next = head
        slow = prev
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        slow.next = slow.next.next
        return prev.next


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), ListNode(1, ListNode(2, ListNode(4, ListNode(5))))),
    ]
    for head, expected in test_cases:
        assert solution.deleteMiddle(head) == expected
