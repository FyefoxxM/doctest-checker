# Quick Start Guide

## Installation
```bash
# Clone or download this project
cd doctest-checker
```

No dependencies to install! Uses only Python standard library.

## Basic Usage

### Test a single file
```bash
python main.py demo.py
```

### Test entire project
```bash
python main.py .
```

### Test specific directory
```bash
python main.py /path/to/your/code
```

## What Gets Tested?

Any code in your docstrings that uses the `>>>` format:

```python
def my_function(x):
    """
    Do something with x.
    
    Example:
        >>> result = 5 + 3
        >>> result
        8
    """
    return x * 2
```

## Understanding the Output

### Passed Example
```
✓ Passed: 1
```
The code ran without errors.

### Failed Example
```
✗ Failed: 1

File: myfile.py
Location: function 'calculate' (line 42)
Error: ZeroDivisionError: division by zero
Code:
  result = 10 / 0
```

Shows you:
- Which file
- Which function/class
- What error occurred
- The code that failed

## Exit Codes

- `0` - All tests passed
- `1` - One or more tests failed

Use in CI/CD:
```bash
python main.py . || echo "Documentation examples are broken!"
```

## Tips for Writing Good Doctest Examples

### ✅ DO: Keep examples self-contained
```python
>>> x = 5
>>> y = 3
>>> x + y
8
```

### ❌ DON'T: Reference undefined functions
```python
>>> result = my_function()  # my_function isn't imported!
```

### ✅ DO: Use simple, demonstrative code
```python
>>> data = [1, 2, 3]
>>> sum(data)
6
```

### ❌ DON'T: Write complex multi-step examples
```python
>>> # Too complex for a simple doctest
>>> import requests
>>> response = requests.get('https://api.example.com')
>>> data = response.json()
```

## Common Issues

### "NameError: name 'X' is not defined"
Your doctest example references a function/class without importing it.

**Solution:** Make examples self-contained or use Python's built-in `doctest` module which has better import handling.

### "No doctest examples found"
Your docstrings don't use the `>>>` format, or you're scanning the wrong directory.

**Solution:** Add examples like:
```python
"""
Example:
    >>> x = 1 + 1
    >>> x
    2
"""
```

## Next Steps

1. Run it on your own projects
2. Fix any broken examples
3. Add to your CI/CD pipeline
4. Share with your team

## Need More Features?

This is a simple tool. For production use, consider:
- Python's built-in `doctest` module
- `pytest --doctest-modules`
- Sphinx documentation testing

This tool is perfect for quick checks and learning how doctests work!
