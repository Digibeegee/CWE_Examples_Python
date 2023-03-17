import pickle

#Deserialization of Untrusted Data

def insecure_deserialization():
    f = open("demo.pickle","rb")
    na = pickle.load(f)
    return na
if __name__ == '__main__':
    print(insecure_deserialization())