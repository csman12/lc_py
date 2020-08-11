"""
lc146-lru_cache.py:
Design and implement a data structure for Least Recently Used (LRU) cache. 
It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, 
it should invalidate the least recently used item before inserting a new item.
The cache is initialized with a positive capacity.
Follow up: Could you do both operations in O(1) time complexity?

Example:
LRUCache cache = new LRUCache( 2 /* capacity */ );
cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
"""

class LRUCache:
    def __init__(self, capacity: int):
        if not capacity: return None
        self._capacity = capacity
        self._size = 0
        self._ll_head = None # MRU node
        self._ll_tail = None # LRU node
        self._dict_ll = {}

    def get(self, key: int) -> int:
        node = self._dict_ll.get(key)
        if node:
            self._move_to_front(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if self._dict_ll.get(key):
            node = self._dict_ll[key]
            node.val = value
            self._move_to_front(node)
            return

        if self._size < self._capacity:
            node = ListNode(key, value)
            self._size += 1
            self._dict_ll[key] = node
            self._add_head_node(node)
            return

        if self._capacity < 1:
            return
            
        if self._capacity == 1:
            node = ListNode(key, value)
            del self._dict_ll[self._ll_head.key]
            del self._ll_head
            self._dict_ll[key] = node
            self._ll_head = node
            return

        # remove LRU from dict, replace tail and move to front
        del self._dict_ll[self._ll_tail.key]
        node = ListNode(key, value)
        self._dict_ll[key] = node
        self._replace_tail_node(node)
        self._move_to_front(self._ll_tail)
        return

    def _add_head_node(self, node):
        if self._ll_head == None and self._ll_tail == None:
            self._ll_head = node
            node.next = None
            node.prev = None
        elif self._ll_tail == None:
            self._ll_tail = self._ll_head
            self._ll_tail.next = node
            self._ll_head = node
            self._ll_head.prev = self._ll_tail
            self._ll_head.next = None
        else:
            self._ll_head.next = node
            node.prev = self._ll_head
            self._ll_head = node

    def _move_to_front(self, node):
        if self._capacity < 2: return
        else:
            if node is self._ll_head:
                return
            elif node is self._ll_tail:
                node.next.prev = None
                self._ll_tail = node.next
                self._ll_head.next = node
                node.next = None
                node.prev = self._ll_head
                self._ll_head = node
            else: # de-link and move to head
                node.next.prev = node.prev
                node.prev.next = node.next
                node.prev = self._ll_head
                self._ll_head.next = node
                node.next = None
                self._ll_head = node

    def _replace_tail_node(self, node):
        tail = self._ll_tail
        node.next = tail.next
        tail.next.prev = node
        self._ll_tail = node
        del tail

    def _print_list(self):
        node = self._ll_head
        node_cnt = 1
        print("Printing out node list:")
        while node != None:
            print("Node", node_cnt, ";  key", node.key, ";  val", node.val)
            node_cnt += 1
            node = node.prev
        print("End of node list!")

class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


def main():
    # ["LRUCache","put","put","get","put","get","put","get","get","get"]
    # [[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]
    cache = LRUCache(2)
    cache.put(1, 1)
    cache._print_list()
    cache.put(2, 2)
    cache._print_list()
    print("Return of get 1:", cache.get(1))
    cache.put(3, 3)
    cache._print_list()
    print("Return of get 2:", cache.get(2))
    cache.put(4, 4)
    cache._print_list()
    print("Return of get 1:", cache.get(1))
    print("Return of get 3:", cache.get(3))
    print("Return of get 4:", cache.get(4))

if __name__ == "__main__":
    main()