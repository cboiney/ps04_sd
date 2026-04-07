#tests for special_delivery

from special_delivery import run_file

#second is worth going to first (provided example)
def test_1():
    assert(run_file("input1.txt") == "2 1")

#in order
def test_2():
    assert(run_file("input2.txt") == "1 2")

#one stop
def test_3():
    assert(run_file("input3.txt") == "1")

#big heavy package at the end of the road
def test_4():
    assert(run_file("input4.txt") == "3 1 2")