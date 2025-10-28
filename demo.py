"""
Demo file to show the doctest checker in action.
"""


def add(a, b):
    """
    Add two numbers together.
    
    Example:
        >>> x = 5 + 3
        >>> print(x)
        8
    """
    return a + b


def multiply(x, y):
    """
    Multiply two numbers.
    
    Example:
        >>> result = 10 * 5
        >>> result == 50
        True
    """
    return x * y


def broken_example():
    """
    This function has a broken doctest example.
    
    Example:
        >>> undefined_function()
        42
    """
    pass


def another_broken():
    """
    Another broken example - division by zero.
    
    Example:
        >>> x = 1 / 0
        >>> print(x)
    """
    pass


class Calculator:
    """
    A simple calculator class.
    
    Example:
        >>> calc = Calculator()
        >>> # This should work!
    """
    
    def __init__(self):
        self.value = 0
    
    def add(self, n):
        """
        Add to the current value.
        
        Example:
            >>> val = 5 + 10
            >>> val
            15
        """
        self.value += n
        return self.value
