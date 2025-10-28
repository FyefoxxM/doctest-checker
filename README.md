# DocTest Checker

A simple tool to validate code examples in Python docstrings.

## What It Does

Scans your Python code for doctest examples (the `>>>` format in docstrings) and runs them to make sure they actually work.

## Why Use This?

Ever written documentation with code examples that broke after you refactored your code? This tool catches that before your users do.

## Installation

No installation needed! Just Python 3.6+

```bash
git clone <your-repo>
cd doctest-checker
```

## Usage

Check a single file:
```bash
python main.py demo.py
```

Check an entire directory:
```bash
python main.py /path/to/your/project
```

Check current directory:
```bash
python main.py .
```

## Example Output

```
============================================================
DocTest Checker - Validating Code Examples
============================================================

Scanning directory: /home/user/project

Found 10 Python file(s)
Found 25 doctest example(s)

============================================================
Running Tests...
============================================================

FAILED EXAMPLES:

  File: utils.py
  Location: function 'calculate' (line 42)
  Error: ZeroDivisionError: division by zero
  Code:
    result = 10 / 0

============================================================
SUMMARY
============================================================
Total Examples: 25
✓ Passed: 24
✗ Failed: 1
============================================================
```

## How to Write Doctest Examples

Use the `>>>` format in your docstrings:

```python
def add(a, b):
    """
    Add two numbers.
    
    Example:
        >>> x = 5 + 3
        >>> x
        8
    """
    return a + b
```

## Limitations

**This is a simple tool.** It won't:
- Handle examples that need imports
- Check expected output (it only checks if code runs without errors)
- Run in isolated environments (uses `exec()`)
- Handle examples that depend on prior state

For production use, consider Python's built-in `doctest` module or tools like `pytest --doctest-modules`.

## Project Structure

```
doctest-checker/
├── scanner.py   # Finds Python files
├── parser.py    # Extracts doctest examples
├── runner.py    # Executes examples
├── main.py      # Orchestrates everything
├── demo.py      # Example file with tests
└── README.md    # This file
```

## Why I Built This

To demonstrate:
1. **Technical skills:** AST parsing, code execution, CLI tools
2. **Writing skills:** Clear documentation and explanations
3. **Practical value:** Solves a real problem developers face

## Blog Post

Read the full breakdown: [Building a Doctest Checker in Python](<your-blog-link>)

## License

MIT
