
class Solution :
    def rearrangeString(self, S):
        #code here
        S = "aaabb" # geeksforgeeks
        freqDict = {}
        result = [S[0]]

        for i in range(1,len(S)):
            currChar = S[i] 
            prevChar = result[-1]
            
            if prevChar != currChar :
                result.append(currChar)
                
                # Check if prev element exist in dict then add and substract
                if (prevChar in freqDict) and (freqDict[prevChar] != 0):
                    result.append(prevChar)
                    freqDict[prevChar] -= 1
                    
                continue
            
            # in case doesn't exist then simply add it in dict
            if currChar in freqDict:
                freqDict[currChar] += 1
            else:
                freqDict[currChar] = 1
        
        #check dict key has any active value
        print(freqDict)
        #print(result)
        print(''.join(result))
        for val in freqDict.values():
            if val > 0:
                return ""
        
        return ''.join(result)
            
    
