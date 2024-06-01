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
        # edge case of the LL being empty
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        # adding a new node to the end of the list
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
    
    # pop method for the LL class
    def pop(self):
        if self.length == 0:
            return None
        pre = self.head
        temp = self.head
        # this while loop lasts until temp
        # First we assign pre to temp
        # temp moves to the next node, while pre remains at the prev node
        # this continues until temp hits None & pre is before last node
        while(temp.next):
            pre = temp
            temp = temp.next
        # move tail back a node
        self.tail = pre
        # remove connection to last node
        self.tail.next = None
        # reduce length of LL
        self.length -= 1
        # now we check if the length is 0
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp.value
    
    # adding a node to a LL
    def prepend(self, value):
        new_node = Node(value)
        # checking whether the linked list is empty
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
        # making new node point to the first node in the LL
           new_node.next = self.head
        # moving head to the new node
           self.head = new_node
        self.length += 1
        return True
    
    # popping a node from the LL
    def pop_first(self):
        # can't pop from a empty list
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        # after removal, if LL is left empty than tail is set to None
        if self.length == 0:
            self.tail = None
        return temp
    
    # get function for my LL class
    def get(self, index):
        # grabbing a edge case
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        # we use a _ instead of a variable i because we don't need  it in the for loop
        for _ in range(index):
            temp = temp.next
        return temp.value
        
                
        
print("Testing out my constructor class for my Linked List by creating a node:")
my_LL = LinkedList(1)

my_LL.print_list()

print("Testing out my append func for my Linked List by adding node 4:")
my_LL.append(4)
my_LL.print_list() 

print("Testing out my pop func for my Linked List by removing the last node")
my_LL.pop()
my_LL.print_list() 

print("Testing out my prepend func for my Linked List by adding the node 3 to the front of the LL")
my_LL.prepend(3)
my_LL.print_list() 

print("Testing out my pop func for my Linked List by removing the first node")
my_LL.pop_first()
my_LL.print_list() 

print("Testing out my get func for my Linked List by printing the index of 2")
my_LL.append(4)
my_LL.append(8)
print(my_LL.get(2)) 

