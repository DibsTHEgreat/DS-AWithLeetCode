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
    
    # appending an item to the end of the list
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
        
        
print("Testing out my constructor class for my Linked List by creating a node:")
my_LL = LinkedList(1)

my_LL.print_list()

print("Testing out my append func for my Linked List by adding node 4:")
my_LL.append(4)
my_LL.print_list() 