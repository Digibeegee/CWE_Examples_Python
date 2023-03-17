if __name__ == '__main__':
    MAX_SIZE=100
    #placing checks for 0, null and maximum size
    width=int(input("Enter width"))
    height=int(input("Enter height"))
    if(width == None or height == None ):
        print("No value present")
    if(width>MAX_SIZE or height>MAX_SIZE or width==0 or height == 0):
        print("Value Invalid: Die evil hacker!")
    else:
        board=[[0 for x in range(width)] for x in range(height)]