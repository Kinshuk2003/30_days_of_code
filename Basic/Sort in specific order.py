class Solution:
    def sortIt(self, arr, n):
        arr.sort()
        odd=[]
        even=[]
        for i in arr:
            if i%2==0:
                even.append(i)
            else:
                odd.insert(0,i)
        for i in range(0,n):
            if odd != []:
                arr[i]=odd.pop(0)
            else:
                arr[i]=even.pop(0)



#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        ob = Solution()
        ob.sortIt(a, n)
        print(*a)

        T -= 1


if __name__ == "__main__":
    main()





    
# } Driver Code Ends
