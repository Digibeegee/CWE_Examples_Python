import sys

#integer overflow in python is not possible since it is treated as long integer since python3

def incrememnt(a):
    return a+1

if __name__ == '__main__':
    print(incrememnt(90))
    print(sys.float_info.max)
    print(incrememnt(sys.float_info.max))
    print(sys.float_info.min)
    print(sys.float_info.min-1)