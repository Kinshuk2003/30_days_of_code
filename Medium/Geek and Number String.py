class Solution:
    def minLength(self, s, n):
        ans=[int(i) for i in s]
        stack=[]
        for i in ans:
            if stack == []:
                stack.append(i)
            elif stack[-1]%2==0:
                if stack[-1] == 0 and i ==9:
                    stack.pop()
                elif i == (stack[-1]-1):
                    stack.pop()
                else:
                    stack.append(i)
            else:
                if stack[-1] == 9 and i ==0:
                    stack.pop()
                elif i == (stack[-1]+1):
                    stack.pop()
                else:
                    stack.append(i)
        
        return len(stack)
