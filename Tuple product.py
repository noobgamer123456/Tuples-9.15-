def sqr(t,n):
    sq = ()
    
    for i in range(0, len(t)):
        
        x = t[i] * n
        sq = sq + (x,)
        
    return sq

tup =(1,2,3,4,5,6)
num = 7
print(sqr(tup,num))