def fib(n):
    a,b, = 1,1 
    for i in range(n):
        a,b = a+b,a
        return a

int fib(int n)
{
    int tmp i,a,b;
    a=b=1;
    for (i=0; i<n;i++){
            tmp  a; a+=b; b = tmp;
}
return a;
}

cdef extern from "fact.h":
        int _fact "fact"(int)

def fact(int n):
    return _fact(n)



def fib(int n):
    cdef int i,a,b
    a,b= 1 1
    for i in range(n):
        a,b = a+b,a
        return a
