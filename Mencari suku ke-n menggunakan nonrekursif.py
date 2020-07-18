def suku(U0,n):
    if n>0:
        for i in range(1,n+1):
            U0+=2019
            print('tracing n = ',i,' dan Un = ',U0)
        return U0
    else:
        for j in range(-1,-n-1):
            U0-=2019
            print('tracing n = ',-j-2,' dan Un = ',U0)
        return U0

looping ='y'
while looping == 'y':
    U0=int(input('Masukkan U0 = '))
    n=int(input('Masukkan n = '))
    if (U0 < n):
        suku(U0+1,n)
    else:
        suku(U0-1,n)
    looping=input('Lanjut = ')

