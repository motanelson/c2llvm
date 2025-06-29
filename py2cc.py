from setuptools import setup
from Cython.Build import cythonize


print("\033c\033[43;30mgive me a .py file to traslate....")
a=input()
setup(
    name='Hello world app',
    ext_modules=cythonize(a),
)