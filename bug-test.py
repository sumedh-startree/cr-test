# broken_buggy_example.py  -- intentionally wrong

import inspect
# NOTE: I *forgot* to import wraps on purpose
# from functools import wraps

def dummy(fn):
    # Oops: using @wraps but didn't import it — NameError will occur when this decorator is applied.
    @wraps(fn)
    def wrapper(a):                # BUG: accepts only one arg, but original functions expect two
        print("in wrapper (should call original)")
        # BUG: uses 'b' which is not defined in this scope -> NameError at call time
        return fn(a, b)
    # BUG: mistakenly returning the original function instead of the wrapper
    return fn

@dummy
def test1(a, b):
    """simple add"""
    return a + b

@dummy
# comment placed between decorator and def (keeps surprise)
def test2(a, b):
    """simple multiply"""
    return a * b

def print_source(fn):
    src, line = inspect.getsourcelines(fn)
    print(f"{fn.__name__} starts at line {line}")
    print("".join(src))
    print("-" * 40)

# This will behave oddly: because dummy returned `fn` not `wrapper`, inspect will show the original function,
# but other runtime problems (wraps missing / undefined b) will still break things elsewhere.
print_source(test1)
print(test1(1, 2))   # Expect 3 but this may fail or behave unexpectedly
