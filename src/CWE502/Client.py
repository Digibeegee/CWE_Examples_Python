import pickle
def serialize_exploit():
    name = {"name":"Prerona","pos":"Software Engineer"}
    f = open("demo.pickle","wb")
    safecode = pickle.dump(name,f)
    return safecode
if __name__ == '__main__':
    safecode = serialize_exploit()