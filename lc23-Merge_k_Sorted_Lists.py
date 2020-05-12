"""
// lc23-Merge_k_Sorted_Lists.cpp : Merge k sorted linked lists and return it as 
// one sorted list. 

// Example:
//    Input:
//    [
//	    1->4->5,
//	    1->3->4,
//	    2->6
//    ]
//    Output: 1->1->2->3->4->4->5->6
"""
from queue import PriorityQueue

def main():
    #test_k_sorted_lists = [ create_test_list(1,5,9), create_test_list(2,4,6), create_test_list(3,7,8) ]
    test_k_sorted_lists = [ create_test_list(), create_test_list(2,4,6), create_test_list(3,7,8) ]
    sorted_list_result = Solution.mergeKLists(Solution(), test_k_sorted_lists)
    print("Result list is: {}".format(ListNode_to_str(sorted_list_result)))

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def create_test_list(*args):
    if not args: return None
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
    def mergeKLists(self, lists: list) -> ListNode:
        if not lists: return None
        setattr(ListNode, "__lt__", lambda self, other: self.val <= other.val)
        pq = PriorityQueue()
        head = ListNode(0)
        itr = head
        for i in range(len(lists)):
            if not isinstance(lists[i], ListNode): continue
            pq.put((lists[i].val, lists[i]))

        while not pq.empty():
            val, pq_top = pq.get()
            itr.next = pq_top
            itr = itr.next
            if pq_top.next:
                pq.put((pq_top.next.val, pq_top.next))
        
        rtn = head.next
        del head
        return rtn

if __name__ == '__main__':
    main()