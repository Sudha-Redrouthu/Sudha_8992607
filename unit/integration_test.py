# import addition
# import multiplication
import calculator
def test_multiplication_addition():
    # Test multiplying the result of adding two numbers with another number
    assert calculator.multiply(calculator.add(2, 3), 4) == 20
# New integration test cases
def test_addition_and_subtraction():
    # Test adding two numbers and then subtracting a third number
    assert calculator.subtract(calculator.add(5, 5), 3) == 7
def test_subtraction_and_division():
    # Test subtracting two numbers and then dividing the result by a third number
    assert calculator.divide(calculator.subtract(11, 5), 3) == 2
def test_multiplication_and_division():
    # Test multiplying two numbers and then dividing the result by a third number
    assert calculator.divide(calculator.multiply(4, 4), 4) == 4
def test_chained_operations():
    # Test a chain of operations: add two numbers, subtract a third, and multiply by a fourth
    assert calculator.multiply(calculator.subtract(calculator.add(3, 3), 4), 5) == 10
def test_division_error_handling():
    # Test division by zero error handling
    try:
        calculator.divide(calculator.subtract(10, 10), 0)
    except ValueError as value:
        assert str(value) == "Cannot divide by zero"
    else:
        assert False, "Expected ValueError"
##Unit testing

# def test_addition():
#     assert calculator.add(2, 3) == 5
#
# def test_subtraction():
#     assert calculator.subtract(5, 3) == 2
#
# def test_multiplication():
#     assert calculator.multiply(2, 3) == 6
#
# def test_division():
#     assert calculator.divide(6, 3) == 2
#
# def test_divide_by_zero():
#     try:
#         calculator.divide(6, 0)
#     except ValueError as e:
#         assert str(e) == "Cannot divide by zero"
#     else:
#         assert False, "Expected ValueError"
#
#
#
