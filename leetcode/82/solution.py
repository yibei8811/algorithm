# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        ans = None
        node = None
        pre_val = None
        while head is not None:
            if (pre_val is None or head.val != pre_val) and (head.next is None or head.val != head.next.val):
                if ans is None:
                    ans = head
                    node = ans
                else:
                    node.next = head
                    node = node.next
            pre_val = head.val
            head = head.next
        if node is not None:
            node.next = None
        return ans


# node7 = ListNode(5)
# node6 = ListNode(4,node7)
# node5 = ListNode(4,node6)
# node4 = ListNode(3,node5)
# node3 = ListNode(3,node4)
node3 = ListNode(2)
node2 = ListNode(2,node3)
head = ListNode(1,node2)
print(Solution().deleteDuplicates(head))
