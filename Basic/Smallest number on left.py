# User function Template for Python3

class Solution:
    def leftSmaller(self, n, a):
        stack=[]
        ans=[]
        for i in range(n):
            while( stack !=[] and stack[-1]>=a[i]):
                stack.pop()
            
            if stack==[]:
                ans.append(-1)
            else:
                ans.append(stack[-1])
            
            stack.append(a[i])
        
        return ans
