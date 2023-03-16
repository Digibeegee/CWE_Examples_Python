import pickle
def insecure_deserialization():
    f = open("D:\Codeguru\CWE_Examples_Python\\resources\demo.txt","rb")
    na = pickle.load(f)
    return na

print(insecure_deserialization())