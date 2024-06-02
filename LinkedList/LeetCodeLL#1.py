# LeetCode 1: Find Middle Node
# If the linked list has an even number of nodes, return the first node of the second half of the list.
# Keep in mind the following requirements:
# The method should use a two-pointer approach, where one pointer (slow) moves one node at a time and the other pointer (fast) moves two nodes at a time.
# When the fast pointer reaches the end of the list or has no next node, the slow pointer should be at the middle node of the list.
# The method should return the middle node or the first node of the second half of the list if the list has an even number of nodes.
# The method should only traverse the linked list once.  In other words, you can only use one loop.

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True   

    # Leetcode work

    def find_middle_node(self):
        slow = self.head
        fast = slow
        
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next
            fast = fast.next
        
        return slow

# Testing my function:
print("Testing out odd list:")
mylist = LinkedList(1)
mylist.append(2)
mylist.append(3)
mylist.append(4)
mylist.append(5)

print( mylist.find_middle_node().value )

print("Testing out even list:")
mylist2 = LinkedList(1)
mylist2.append(2)
mylist2.append(3)
mylist2.append(4)

print( mylist2.find_middle_node().value )