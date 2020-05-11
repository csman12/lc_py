"""
  lc2-add_two_numbers.py : 
  You are given two non-empty linked lists representing two non-negative integers. 
  The digits are stored in reverse order and each of their nodes contain a single 
  digit. Add the two numbers and return it as a linked list.
  You may assume the two numbers do not contain any leading zero, except the 
  number 0 itself.

  Example:
     Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
     Output : 7 -> 0 -> 8
	  Explanation : 342 + 465 = 807.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def main():
    #test_list_1 = create_test_list(2,4,3)
    #test_list_2 = create_test_list(5,6,4)
    test_list_1 = create_test_list(5)
    test_list_2 = create_test_list(5)
    print("Test list 1 is: {}".format(ListNode_to_str(test_list_1)))
    print("Test list 2 is: {}".format(ListNode_to_str(test_list_2)))
    
    sln = Solution()
    result = sln.addTwoNumbers(test_list_1, test_list_2)
    print("Result is: {}".format(ListNode_to_str(result)))

def create_test_list(*args):
    if args is None: return None
    head = ListNode(args[0])
    itr = head
    for i in range(1, len(args)):
        itr.next = ListNode(args[i])
        itr=itr.next
    return head

def ListNode_to_str(l: ListNode):
    num_list = []
    itr = l
    while itr is not None:
        num_list.append(str(itr.val))
        itr = itr.next
    return " ".join(num_list)


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 or not l2: return None
        head = ListNode(0)
        itr = head
        carry = 0
        while True:
            if l1 and l2:
                val = l1.val + l2.val + carry
                l1 = l1.next
                l2 = l2.next
            elif l1:
                val = l1.val + carry
                l1 = l1.next
            elif l2:
                val = l2.val + carry
                l2 = l2.next
            else:
                val = carry
            if val > 9: 
                carry = 1
                val = val - 10
            else:
                carry = 0
            itr.val = val
            if l1 or l2 or carry:
                itr.next = ListNode(0)
                itr = itr.next
                continue
            else:
                break

        return head

if __name__ == '__main__':
    main()