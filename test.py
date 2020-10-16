with open('temp.txt','w') as open:
    n=1
    x=0
    for i in range(10):
        print('P'+str(n)+'  = '+'P['+str(x)+"], ",file=open, end='' )
        n+=1
        x+=1

    print(' ', file=open)

    n=1
    for i in range(10):
        print('P'+str(n)+' = 0 ',file=open,  )
        n+=1


n=50