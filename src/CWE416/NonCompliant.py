import gc

#Use after free

class CWE416:
    def msg(self):
        print('Greetings User')

obj=CWE416()
obj.msg()
del obj
gc.collect()
obj.msg()