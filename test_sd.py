#tests for special_delivery

from special_delivery import run_file

def test_1():
    assert(run_file("input1.txt") == "2 1")

def test_2():
    assert(run_file("input2.txt") == "1 2")

def test_3():
    assert(run_file("input3.txt") == "1")