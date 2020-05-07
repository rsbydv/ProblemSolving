
'''
Hello Its me 
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


  

