from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

ext = Extension("particle", ["particle.pyx", "particle_extern.cpp"], language="c++")

setup(
    cmdclass = {'build_ext': build_ext},
    ext_modules = [ext],
)
