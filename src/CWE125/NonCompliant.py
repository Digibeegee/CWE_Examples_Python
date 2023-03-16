
#out of bounds read

L=[-1,2,-3,4,-5]
read= True
while read:
    ele=int(input('Enter element to read:   '))
    print(L[ele])
    read=bool(input('read more?'))