if __name__ == '__main__':
    L=[-1,2,-3,4,-5]
    read= True
    while read:
        ele=int(input('Enter element to read:   '))
        #adding index check
        if ele>=len(L):
            print("Invalid index!!")
            continue
        print(L[ele])
        read=bool(input('read more?'))