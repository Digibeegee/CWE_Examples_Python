import builtins
import io
import pickle

safe_builtins = {
    'range',
    'complex',
    'set',
    'frozenset',
    'slice',
}

class RestrictedUnpickler(pickle.Unpickler):

    def find_class(self, module, name):
        # Only allow safe classes from builtins.
        if module == "builtins" and name in safe_builtins:
            return True
        # Forbid everything else.
        raise pickle.UnpicklingError("global '%s.%s' is forbidden" %
                                     (module, name))

def insecure_deserialization():

    # Compliant: Untrusted object is validated before deserialization.
    f = open("demo.pickle","rb")
    if RestrictedUnpickler(f):
        na = pickle.load(f)
        return na
if __name__ == '__main__':
    print(insecure_deserialization())