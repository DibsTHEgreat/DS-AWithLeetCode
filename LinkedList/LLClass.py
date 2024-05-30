# This class represents a Node
class Node:
    # constructor for class
    def __init__(self, value):
        self.value = value
        self.next = None

# This class represents a Linked-List
class LinkedList:
    # constructor for class
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    # prints a linked list
    def print_list(self):
        # using temp we can navigate through the LL
        temp = self.head
        # stop running the loop once we hit the end
        while temp is not None:
            print(temp.value)
            # we assign temp the temp.next, so move along
            # the list
            temp = temp.next
        
print("Testing out my constructor class for my Linked List by creating a node:")
my_LL = LinkedList(1)

my_LL.print_list()