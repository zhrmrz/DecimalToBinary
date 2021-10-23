class Sol:
    def DecimalToBinary(self,n):
        bin_n=list(bin(n)[2:])
        l=[i for i,x in enumerate(bin_n) if x=='1']
        max=0
        if len(l)==1:
            return l[0]
        for i in range(1,len(l)):
            if max<l[i]-l[i-1]:
                max=l[i]-l[i-1]
        return max
if __name__ == '__main__':
    p = Sol()
    print(p.DecimalToBinary(n=22))
