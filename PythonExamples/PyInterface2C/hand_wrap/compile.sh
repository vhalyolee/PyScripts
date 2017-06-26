#!/bin/sh

gcc -c -fpic fact.c fact_wrap.c -I. -I/usr/include/python2.7
gcc -shared fact.o fact_wrap.o -L /usr/lib/python2.7/site-packages/configobj -I python2.7 -o example.so

