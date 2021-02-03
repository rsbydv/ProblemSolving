   
#               1. Transfiguration 
# Easy Accuracy: 100.0% Submissions: 452 Points: 2
# Professor McGonagall teaches transfiguration at Hogwarts. She has given Harry the task of changing himself into a cat. She explains that the trick is to analyze your own DNA and change it into the DNA of a cat. The transfigure spell can be used to pick any one character from the DNA string, remove it and insert it in the beginning. 
# Help Harry calculates minimum number of times he needs to use the spell to change himself into a cat.

# Example 1:

# Input: 
# A = "GEEKSFORGEEKS" 
# B = "FORGEEKSGEEKS"
# Output: 3
# Explanation:The conversion can take place 
# in 3 operations:
# 1. Pick 'R' and place it at the front, 
#   A="RGEEKSFOGEEKS"
# 2. Pick 'O' and place it at the front, 
#   A="ORGEEKSFGEEKS"
# 3. Pick 'F' and place it at the front, 
#   A="FORGEEKSGEEKS"
# Example 2:

# Input: 
# A = "ABC" 
# B = "BCA"
# Output: 2
# Explanation: The conversion can take place 
# in 2 operations:
# 1. Pick 'C' and place it at the front, 
#   A = "CAB"
# 2. Pick 'B' and place it at the front, 
#   A = "BCA"
# Your Task:  
# You don't need to read input or print anything. Complete the function transfigure() which takes strings A and B as input parameters and returns the minimum number of spells needed. If it is not possible to convert A to B then return -1.

# Expected Time Complexity: O(max(|A|, |B|))
# Expected Auxiliary Space: O(1)

# Constraints:
# 1 ≤ |A|, |B| ≤ 105
# A and B consists of lowercase and uppercase letters of english alphabet only.

# Topic Tags
# Related Courses





class Solution:
    def transfigure(self, A, B): 
        # code here 
        if A==B: return 0 #strings are same
        if len(A)!=len(B): return -1 # strings are not with equal length
        
        
        di = {}
        for char in A:
            if char in di:
                di[char] += 1
            else: 
                di[char] = 1
        
        #check if all the character of A exist in B
        for char in B:
            if char not in di:
                return -1
            else:
                di[char] -= 1
        
        #check is there any pending char in A
        for char in di:
            if di[char]:
                return -1
        
        n = len(A)
        i=j=n-1
        result = 0
        
        while i>=0:
            while i>=0 and A[i]!=B[j]:
                result += 1
                i -= 1
            i-=1
            j-=1
            
        return result
            
                
            
 
    
