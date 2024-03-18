#등차수열
def seq(n):
    if n==1:
        return 1
    else:
        return seq(n-1)+3
    
print(seq(10))

#하노이 탑
def move(n,src, tmp, dest):
    if (n>0):
        move(n-1,src,dest,tmp)
        print("move %d from %c to %c" % (n,src,dest))
        move(n-1,tmp,src,dest)

#move(3,'a','b','c')

#2의 제곱
def pow2(n):
    if n==0:
        return 1
    else:
       2*pow2(n-1)

pow2(100)
       



    
    
