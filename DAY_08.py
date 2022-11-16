command = (input('Type \'encode\' to encrypt, type \'decrypt\' to decode:'))

alphabets = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z]


if command == 'encode':
    message = (input('Type your message'))
    code1 = [ ch for ch in message]
    print(code1)
elif command == 'decode':
    print('This could not be decoded')
else:
    print('This is all we had')