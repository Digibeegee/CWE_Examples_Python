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
    obj.msg()