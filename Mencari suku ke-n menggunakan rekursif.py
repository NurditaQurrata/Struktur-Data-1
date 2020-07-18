def suku(U0,n,x):
    if(U0<n):
        x+=2019
        print('tracing i = ',U0,' dan Un = ',x)
        return suku(U0+1,n,x)
    elif(U0>n):
        x-=2019
        print('tracing i = ',U0,' dan Un = ',x)
        return suku(U0-1,n,x)
    elif(U0==n):
        if(n>0):
            x+=2019
        else:
            x-=2019
        print('tracing i = ',U0,' dan Un = ',x)
        print('hasil Un = ',x)

looping = 'y'
while looping =='y':
    U0=int(input('Masukkan U0 = '))
    n=int(input('Masukkan n = '))
    if (U0 < n):
        suku(U0+1,n,0)
    else:
        suku(U0-1,n,0)
    looping=input('Lanjut = ')
