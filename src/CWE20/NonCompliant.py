if __name__ == '__main__':
    MAX_SIZE=100
#Improper Input Validation
    width=int(input("Enter width"))
    height=int(input("Enter height"))

    if(width>MAX_SIZE or height>MAX_SIZE):
        print("Value too large: Die evil hacker!")
    board=[[0 for x in range(width)] for x in range(height)]