# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        node = l1
        power = 1
        num1 = 0
        while node != None:
            print(type(node), type(node.val))
            num1 += (int)(node.val) * power
            power *= 10
            node = node.next
        
        node = l2
        power = 1
        num2 = 0
        while node != None:
            num2 += node.val * power
            power *= 10
            node = node.next
        
        resultNum = num1 + num2
        currentItem = ListNode(val = int(str(resultNum)[0]), next = None)
        for i in range(1, len(str(resultNum))):
            newItem = ListNode(val = int(str(resultNum)[i]), next = currentItem)
            currentItem = newItem

        return currentItem