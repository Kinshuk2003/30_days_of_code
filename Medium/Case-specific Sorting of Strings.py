class Solution:

    #Function to perform case-specific sorting of strings.
    def caseSort(self,s,n):
        upper=[]
        lower=[]
        ans=""
        for i in s:
            if (i>='A' and i<='Z'):
                upper.append(i)
            elif (i>= 'a' and i<='z'):
                lower.append(i)
        upper.sort()
        lower.sort()
        i=0
        j=0
        for k in range(0,n):
            if (s[k]>='A' and s[k] <='Z'):
                ans +=upper[i]
                i +=1
            elif (s[k]>='a' and s[k] <='z'):
                ans +=lower[j]
                j +=1
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for tt in range(t):
        n=int(input())
        s=str(input())
        print(Solution().caseSort(s,n))
# } Driver Code Ends
