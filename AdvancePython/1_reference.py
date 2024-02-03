from python1 import dept
dept("I am Electrical Student.")

# When we do it a new __pycache__ folder will created, Now question arises is that why it happen what is it?
# script for code running is (python fileName.py)
# python virtual machine where byte code is executed.
# Basically byte code is low level and plateform independent.
# .pyc--> complied python (frozen binaries)
# cpython-312.pyc --> here cpython is one of the version of python with 312 that is current version.
# .pyc file always works for imported files.


# Let's discuss about python virtual machine.
# isme a continuously ek loop chalta hai jo code to line wise line execute krta hai, that why it is also called python interpreter.
# this is also run time engine.

# Byte code is not machine code.
# It is python specific interpretation
# cpython(standard implementation), jython, iron Python, stackless, etc.
