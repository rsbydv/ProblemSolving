
'''
Given an integer k and a binary search tree, find the floor (less than or equal to) of k, and the ceiling (larger than or equal to) of k. If either does not exist, then print them as None.

Here is the definition of a node for the tree.

class Node:
  def __init__(self, value):
    self.left = None
    self.right = None
    self.value = value

def findCeilingFloor(root_node, k, floor=None, ceil=None):
  # Fill this in.

root = Node(8) 
root.left = Node(4) 
root.right = Node(12) 
  
root.left.left = Node(2) 
root.left.right = Node(6) 
  
root.right.left = Node(10) 
root.right.right = Node(14) 

print findCeilingFloor(root, 5)
# (4, 6)

'''




#A program to find out the ceil in the BST for any given input.
#A value which is smallest but follow the #condition of greater than or equal to the given input.
#return None if won't found any solution

print("Hello and good morning.")

class Node:
  def __init__(self,key):
    self.left = None
    self.right = None
    self.key = key

def get_ceil(root,inp): 
  #Base case
  if root == None:
    return None
  
  #We found an equal key
  if root.key == inp:
    return root.key

  #If root key is smaller
  if root.key < inp:
    return get_ceil(root.right,inp)
  
  #If root key is greater
  if root.key > inp:
    val = get_ceil(root.left,inp)
    if val == None:
      return root.key
    if val <= root.key:
      return val
    return root.key


#Driver program to test above function 
root = Node(8) 
  
root.left = Node(4) 
root.right = Node(12) 
  
root.left.left = Node(2) 
root.left.right = Node(6) 
  
root.right.left = Node(10) 
root.right.right = Node(14) 

for i in range(16): 
  print(i, get_ceil(root,i))



'''
Now we need to write this funstion to find out the floor value in the BST \
for any given input

floor means, A value which is greatest value in the bst which is less than the\
given input value

floor<=input

Cases

1. None Base Case
    if the root is None, return none then 

2. Positive Base Case 
    if value is equal to the given input, ans is root

3. Less than, check left

4. Greater than, check right and last check with the root

'''



def get_floor(root,inp):
    if root == None:
        return None

    if root.key == inp:
        return root.key

    if root.key > inp:
        return get_floor(root.left, inp)

    if root.key < inp:
        val = get_floor(root.right,inp)
        if val == None:
            return root.key
        return val


def insert(root,key):
    if root == None:
        return Node(key)

    if root.key == key:
        return root
    
    if key < root.key:
        if root.left == None:
            child = Node(key)
            root.left = child
            return child
        return insert(root.left,key)
    else:
        if root.right == None:
            child = Node(key)
            root.right = child
            return child
        return insert(root.right,key)


#Driver Code
root = None
root = insert(root, 7)   
insert(root, 10)  
insert(root, 5)  
insert(root, 3)  
insert(root, 6)  
insert(root, 8)  
insert(root, 12) 

print("floor value for the input is ",get_floor(root, 9)) 







  

