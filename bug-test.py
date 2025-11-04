import inspect

def dummy(fn):
    return fn

@dummy
def test1(a, b):
    return a

@dummy
#comment
def test2(a, b):
    return a
#Prints output
print(inspect.getsourcelines(test1))
print("------------------")
print(inspect.getsourcelines(test2))   
