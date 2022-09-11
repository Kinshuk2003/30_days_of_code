class Solution:
    def snakeCase(self, S , n):
        str=''
        for i in range(0,n):
            if S[i]==' ':
                str +='_'
            elif S[i].isupper():
                str +=S[i].lower()
            else:
                str +=S[i]
        return str
