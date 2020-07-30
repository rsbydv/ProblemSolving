'''
You are given a pointer/ reference to the node which is to be deleted from the linked list of N nodes. The task is to delete the node. Pointer/ reference to head node is not given. 
Note: No head reference is given to you.

Input:
First line of input contains number of testcases T. For each testcase, first line of input contains length of linked list and next line contains the data of the linked list. The last line contains the node to be deleted.

Output:
For each testcase, in a newline, print the linked list after deleting the given node.

Your Task:
This is a function problem. You only need to complete the function deleteNode that takes reference to the node that needs to be deleted. The printing is done automatically by the driver code.

Expected Time Complexity : O(n)
Expected Auxilliary Space : O(n)

Constraints:
1 <= T <= 100
1 <= N <= 103

Example:
Input:
2
2
1 2
1
4
10 20 4 30
20
Output:
2
10 4 30

Explanation:
Testcase 1: After deleting 1 from the linked list, we have remaining nodes as 2.
Testcase 2: After deleting 20 from the linked list, we have remaining nodes as 10, 4 and 30.
'''


#User function Template for python3
'''
    Your task is to delete the given node from
	the linked list, without using head pointer.
	
	Function Arguments: node (given node to be deleted) 
	Return Type: None, just delete the given node from the linked list.

	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}

	Contributed By: Nagendra Jha
'''
def deleteNode(curr_node):
    #code here
    if curr_node == None:
        return
    if curr_node.next != None:
        curr_node.data = curr_node.next.data
        curr_node.next = curr_node.next.next
    return
        

'''
Important Note: 

This solution failed in below cases
 if the node to be deleted is head node 
 if the next node of the given node is null

As to do any changes in the current we need to have the reference of the previous node

'''
       