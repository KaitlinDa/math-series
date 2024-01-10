from series import fibonacci, lucas, sum_series

def test_fibonacci():
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3


def test_lucas():
    assert lucas(0) == 2
    assert lucas(1) == 1
    assert lucas(2) == 3
    assert lucas(3) == 4
    assert lucas(4) == 7
   

def test_sum_series():
    assert sum_series(4) == fibonacci(4)  
    assert sum_series(4, 2, 1) == lucas(4)  
    assert sum_series(4, 3, 2) == 12 