import sys
# sys.path.append('../doubly_linked_list')
# from doubly_linked_list import DoublyLinkedList

class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode"""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        new_node = ListNode(value)
        self.length += 1
        if not self.head and not self.tail:
            # empty list, this is head and tail
            self.head = new_node
            self.tail = new_node
        else:
             # We know the list is populated, and we need to update the previous head
             new_node.next = self.head
             self.head.prev = new_node
             self.head = new_node
        # What do we need to think about?
        # What are the scenarios?
        # This needs to be head because we're adding to the head
        # Update previous head
        # increase length
        # Edge cases? -- If self.head is None there is no list and no tail
        # if there is no tail...New becomes new tail as well
        
        

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        value = self.head.value
        self.delete(self.head)
        return value

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        self.length += 1
        if not self.head and not self.tail:
            #Empty list, this head and tail
            self.head = self.tail = ListNode(value)
        else: 
            # We know the list is populated
            self.tail.insert_after(value)
            self.tail = self.tail.next
        # new_node = ListNode(value)
        # self.length += 1
        # if not self.head and not self.tail:
        #     # Empty list this is head and tail
        #     new_node = self.head
        #     new_node = self.tail
        # else:
        #      self.tail.next = new_node
        #      self.tail.prev = self.head
        #      self.tail = new_node

    # """Removes the List's current tail node, making the 
    # current tail's previous node the new tail of the List.
    # Returns the value of the removed Node."""
    def remove_from_tail(self):
        value = self.tail.value
        self.delete(self.tail)
        return value

    # """Removes the input node from its current spot in the 
    # List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        # long way
        # if node is self.head:
        #     return
        # value = node.value
        # if node is self.tail:
        #     self.remove_from_tail()
        # else: 
        #     node.delete()
        #     self.add_to_head(value)
        # shorter way
        self.delete(node)
        self.add_to_head(node.value)


    # """Removes the input node from its current spot in the 
    # List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        # if node is self.tail:
        #     return
        self.delete(node)
        value = node.value
        self.add_to_tail(value)

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
    
        self.length -= 1        
        # If node is both
        if self.head is self.tail:
            self.head = None
            self.tail = None
        

        # If node is head
        elif node is self.head:
            self.head = self.head.next
            node.delete()
        
        # If node is tail
        elif node is self.tail:
            self.tail = self.tail.prev
            node.delete()
        
        # If node is in middle
        else:
             node.delete()   
        
    # """Returns the highest value currently in the list"""
    # def get_max(self):
          # Make max variable
          # Loop through nodes via node.next
          # If node.value is higher update max
          # Return max
    #     pass

class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def push(self, value):
        self.size += 1
        self.storage.add_to_head(value)

    def pop(self):
        if self.size == 0:
            return
        self.size -= 1
        return self.storage.remove_from_head()

    def len(self):
        return self.size
