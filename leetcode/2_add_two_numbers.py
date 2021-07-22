'''
https://leetcode.com/problems/add-two-numbers/

You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def printList(node: ListNode):
    while node!= None:
        print(node.val, end="")
        node = node.next
    print("\n")

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        leftover = 0
        l3 = None
        rtype = None
        while l1 != None and l2 != None:
            value = leftover + l1.val + l2.val
            leftover = 0
            if value > 9:
                leftover = int(value / 10)
                value = value % 10
            if l3 is None:
                l3 = ListNode(value)
                rtype = l3
            else:
                l3.next = ListNode(value)
                l3 = l3.next
            l1 = l1.next
            l2 = l2.next

        lo_node = l2 if l1 is None else l1
        while leftover != 0 and lo_node is not None:
            value = leftover + lo_node.val
            leftover = 0
            if value > 9:
                leftover = int(value / 10)
                value = value % 10
            l3.next = ListNode(value)
            l3 = l3.next
            lo_node = lo_node.next

        if lo_node:
            l3.next = lo_node
        elif leftover != 0:
            l3.next = ListNode(leftover)

        return rtype

def prepareList(num):
    if num == 0:
        return None
    return ListNode(num % 10, prepareList(int(num / 10)))


l1 = prepareList(9999999)
printList(l1)
l2 = prepareList(9999)
printList(l2)

obj = Solution()
result = obj.addTwoNumbers(l1, l2)
printList(result)
