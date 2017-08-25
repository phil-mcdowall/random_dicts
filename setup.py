from distutils.core import setup, Extension
setup(
    py_modules =['weighted_dict'],
    ext_modules=[Extension("randomdict", ["random_weighted/randomdict.c"])]
)