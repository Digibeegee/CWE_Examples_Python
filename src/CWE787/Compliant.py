if __name__ == '__main__':
    #index check
    arr = [0] * 5
    for i in range(len(arr)+1):
        if i<len(arr):
            arr[i]=i*10 + (i-1)
        else:
            print('Out of bounds write detected')
    print(arr)