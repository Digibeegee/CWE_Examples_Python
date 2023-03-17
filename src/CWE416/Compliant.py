import gc

#Use after free

class CWE416:
    def msg(self):
        print('Greetings User')

if __name__ == '__main__':
    obj=CWE416()
    obj.msg()
    del obj
    gc.collect()
    #check if object exists
    if 'obj' in locals() or 'obj' in globals():
        obj.msg()
    else:
        print('Object does not exist')