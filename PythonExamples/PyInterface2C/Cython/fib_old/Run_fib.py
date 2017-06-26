# from inside python you can run this script



import pyximport

pyximport.install() # hooks into the pythons import mechanism

from fib import fib # finds fib.pyx auto compiles

print fib(10)

