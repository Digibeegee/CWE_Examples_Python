#out of bouinds write
if __name__ == '__main__':
    arr = [0] * 5
    for i in range(len(arr)+1):
        arr[i]=i*10 + (i-1)
    print(arr)