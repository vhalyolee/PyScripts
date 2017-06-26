#!/bin/python

from distutils.core import setup, Extension

ext = Extension(name='example', sources=['fact_wrap.c', 'fact.c'])

setup(name="example", ext_modules=[ext])

#python setup.py build 
# for win -- compiler=mingw64
# python setup.py install

#python setup.py build_ext --inplace 
# on windows --compiler=mingw64

