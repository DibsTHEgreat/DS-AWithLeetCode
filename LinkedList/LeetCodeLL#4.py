# LeetCode 4: Partition List
# Implement the partition_list member function for the LinkedList class, which 
# partitions the list such that all nodes with values less than x come before nodes 
# with values greater than or equal to x.

# Note: This linked list class does NOT have a tail which will make this method easier 
# to implement. The original relative order of the nodes should be preserved.

# Keep in mind the following requirements:
# The function partition_list takes an integer x as a parameter and modifies 
# the current linked list in place according to the specified criteria. If the 
# linked list is empty (i.e., head is null), the function should return immediately 
# without making any changes.

# Tips:
# While traversing the linked list, maintain two separate chains: one for values less than 
# x and one for values greater than or equal to x.
# Use dummy nodes to simplify the handling of the heads of these chains.
# After processing the entire list, connect the two chains to get the desired arrangement.

#  Note:
# The solution must maintain the relative order of nodes. For instance, in the first 
# example, even though 8 appears before 5 in the original list, the partitioned list 
# must still have 8 before 5 as their relative order remains unchanged.
# Note:
# You must solve the problem WITHOUT MODIFYING THE VALUES in the list's nodes (i.e., only 
# the nodes' next pointers may be changed.)


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node
        self.length += 1 
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next    
            
    def make_empty(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    # WRITE PARTITION_LIST METHOD HERE #
    #                                  #
    #                                  #
    #                                  #
    #                                  #
    ####################################
    def partition_list(self, x):
        if self.head is None:
            return None
        
        lessThanX = Node(0)
        greaterOrEqualThanX = Node(0)
        prev1 = lessThanX
        prev2 = greaterOrEqualThanX
        current = self.head
        
        while current is not None:
            if current.value < x:
                prev1.next = current
                prev1 = current
            else:
                prev2.next = current
                prev2 = current
            current = current.next
        
        prev1.next = None
        prev2.next = None
        
        prev1.next = greaterOrEqualThanX.next
        self.head = lessThanX.next

ll = LinkedList(1)
ll.append(3)
ll.append(5)
ll.append(2)
ll.append(4)

print("LL before partition_list:")
ll.print_list() # Output: 3 5 8 10 2 1

ll.partition_list(5)

print("LL after partition_list:")
ll.print_list() # Output: 3 2 1 5 8 10