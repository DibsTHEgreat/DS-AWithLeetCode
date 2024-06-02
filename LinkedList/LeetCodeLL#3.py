# LeetCode 3: Find Kth Node From End
# Implement the find_kth_from_end function, which takes the LinkedList (ll) and an integer k as input, and returns the k-th node 
# from the end of the linked list WITHOUT USING LENGTH.

# Keep in mind the following requirements:
# The function should utilize two pointers, slow and fast, initialized to the head of the linked list.
# The fast pointer should move k nodes ahead in the list.
# If the fast pointer becomes None before moving k nodes, the function should return None, as the list is shorter than k nodes.
# The slow and fast pointers should then move forward in the list at the same time until the fast pointer reaches the end of the list.
# The function should return the slow pointer, which will be at the k-th position from the end of the list.


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

def find_kth_from_end(ll, index):
    fast = slow = ll.head
    
    # creating a gap between fast and slow
    for _ in range (index):
        if fast is None:
            return None
        fast = fast.next
        
    # iterating normally, until fast is None
    while fast is not None:
        slow = slow.next
        fast = fast.next
    
    return slow
        


print("Testing code:")
my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)


k = 2
result = find_kth_from_end(my_linked_list, k)

print(result.value)  