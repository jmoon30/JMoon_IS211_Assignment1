# assignment1_part1.py

class ListDivideException(Exception):
    """Custom exception for
        the list divide errors"""
    pass

def list_divide(numbers, divide = 2):
    """Return numbers that are
        divisible from divide."""
    return sum(1 for n in numbers if n % divide == 0)

def test_list_divide():
    """Test the function
        for list_divide"""
    try:
        assert list_divide([1, 2, 3, 4, 5]) == 2
        assert list_divide([2, 4, 6, 8, 10]) == 5
        assert list_divide([30, 54, 63, 98, 100], divide = 10) == 2
        assert list_divide([]) == 0
        assert list_divide([1, 2, 3, 4, 5], 1) == 5
    except AssertionError:
        raise ListDivideException()

if __name__ == '__main__':
    test_list_divide()
    print("All tests passed.")