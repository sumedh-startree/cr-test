import inspect
from functools import wraps

def dummy(fn):
    # Real decorator pattern — preserves original function metadata
    @wraps(fn)
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper

@dummy
def test1(a, b):
    return a

@dummy
# comment
def test2(a, b):
    return a

def print_source(fn):
    source, line = inspect.getsourcelines(fn)
    print(f"Function: {fn.__name__}, starts at line {line}")
    print("".join(source))
    print("-" * 30)

print_source(test1)
print_source(test2)
