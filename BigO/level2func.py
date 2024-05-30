# Creating a simple function to showcase an example of what O(n^2) is

# this function takes in a parameter of n
def the_repeater(n):
    for i in range(n):
        for j in range(n):
            print(i, j)

# Output will show that the function runs (n * n) times
# In this example, it is 10 * 10 times...
the_repeater(10)