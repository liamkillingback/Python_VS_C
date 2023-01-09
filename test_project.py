from ctypes import *
from project import lib

def main():
    test_c_add()
    test_c_sub()
    test_c_div()
    test_c_multiply()
    
def test_c_add():
    assert lib.c_add(2, 4) == 6
def test_c_sub():
    assert lib.c_sub(6, 2) == 4
def test_c_div():
    assert lib.c_div(10, 5) == 2
def test_c_multiply():
    assert lib.c_multiply(2, 20) == 40



if __name__ == '__main__':
    main()
