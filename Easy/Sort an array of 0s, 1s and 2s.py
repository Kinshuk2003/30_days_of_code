class Solution:
    def sort012(self,arr,n):
        count=[0]*3
        for i in arr:
            count[i] +=1
        
        for j in range(1,3):
            count[j] +=count[j-1]
        
        brr=[0]*n
        for i in range(n-1,-1,-1):
            count[arr[i]] -=1
            brr[count[arr[i]]]=arr[i]
        
        for i in range(0,n):
            arr[i] =brr[i]
