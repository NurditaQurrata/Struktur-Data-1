def sigma(i,n,x):
    if(i<n):
        x+=(i**3)-(6*(i**2))+(7*i)-(8)
        print('tracing i = ',i,' dan y = ',float(x))
        return sigma(i+1,n,x)
    elif(i>n):
        x+=(i**3)-(6*(i**2))+(7*i)-(8)
        print('tracing i = ',i,' dan y = ',float(x))
        return sigma(i-1,n,x)
    elif(i==n):
        x+=(i**3)-(6*(i**2))+(7*i)-(8)
        print('tracing i = ',i,' dan y = ',float(x))
        print('hasil perhitungan dengan dengan n = ',n,' : ',float(x))

looping='y'
while looping == 'y':
    n=int(input('Masukkan n = '))
    sigma(1,n,0)
    looping=input('Lanjut = ')
    
