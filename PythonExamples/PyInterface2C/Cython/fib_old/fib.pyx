def fib(int n):
    cdef int a, b, i
    a, b = 1, 1
    for i in range(n):
        a, b = a+b, a
    return a


# This will generate fib.c with Cython and compile with setup.py to make a fib.so
# if you have fib.h.c compile to make fib.so

