# import sys
# sys.path.append('./doubly_linked_list')
from doubly_linked_list import DoublyLinkedList 


class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.limit = limit
        self.size = 0
        self.dict_storage = dict()
        self.list_order = DoublyLinkedList()
    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    
    def get(self, key):
        if key not in self.dict_storage:
            return None
        else:
            node = self.dict_storage[key]
            self.list_order.move_to_end(node)
            return node.value[1]

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        if key in self.dict_storage:
            node = self.dict_storage[key]
            node.value = (key, value)
            self.list_order.move_to_end(node)
            return
        
        if len(self.list_order) == self.limit:
                head_index = self.list_order.head.value[0]
                del self.dict_storage[head_index]
                self.list_order.remove_from_head()

                # add to the list order tail
                self.list_order.add_to_tail((key, value))
                self.dict_storage[key] = self.list_order.tail
        if len(self.list_order) < self.limit:
            self.list_order.add_to_tail((key, value))
            self.dict_storage[key] = self.list_order.tail
    
