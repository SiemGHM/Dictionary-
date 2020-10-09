with open('temp.txt','w') as open:
    n=1
    x=0
    for i in range(10):
        print('M'+str(n)+' = '+'Ms['+str(x)+"], ",file=open, end='' )
        n+=1
        x+=1

    print(' ', file=open)

    n=1
    for i in range(10):
        print('M'+str(n)+' = 0 ',file=open,  )
        n+=1