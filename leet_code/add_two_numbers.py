
# 2

from __future__ import annotations

from typing import Optional


class ListNode(object):

    def __init__(self, val=0, next: Optional[ListNode] = None):
        self.val = val
        self.next = next


class Solution:

    def addTwoNumbers(self, l1: ListNode, l2: ListNode, quotient: int = 0):

        val = l1.val + l2.val + quotient
        quotient = val // 10
        result_node = ListNode(val % 10)

        if (l1.next or l2.next or quotient != 0):
            l1.next = ListNode(0) if not l1.next else l1.next
            l2.next = ListNode(0) if not l2.next else l2.next
            result_node.next = self.addTwoNumbers(l1.next, l2.next, quotient)

        return result_node


if __name__ == '__main__':
    obj_1 = Solution()
    ln_1 = ListNode(2, ListNode(4, ListNode(3)))
    ln_2 = ListNode(5, ListNode(6, ListNode(4)))

    sum_of_l1_l2 = obj_1.addTwoNumbers(ln_1, ln_2)
    print(sum_of_l1_l2.val, sum_of_l1_l2.next.val, sum_of_l1_l2.next.next.val)
