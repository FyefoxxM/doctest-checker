"""
Runner for executing doctest examples and capturing results.
"""
from typing import Dict


def run_example(code: str) -> Dict[str, str]:
    """
    Execute a code example and return the result.
    
    Args:
        code: Python code string to execute
    
    Returns:
        Dict with 'status' ('PASS' or 'FAIL') and optional 'error' message
    
    Example:
        >>> result = run_example('x = 5')
        >>> result['status']
        'PASS'
    """
    try:
        # Create a clean namespace for execution
        namespace = {}
        exec(code, namespace)
        return {'status': 'PASS', 'error': None}
    except Exception as e:
        # Capture the error type and message
        error_msg = f"{type(e).__name__}: {str(e)}"
        return {'status': 'FAIL', 'error': error_msg}


def run_example_verbose(code: str) -> Dict[str, str]:
    """
    Execute code with more detailed error information.
    
    This version is useful for debugging.
    """
    import traceback
    
    try:
        namespace = {}
        exec(code, namespace)
        return {'status': 'PASS', 'error': None, 'traceback': None}
    except Exception as e:
        error_msg = f"{type(e).__name__}: {str(e)}"
        tb = traceback.format_exc()
        return {'status': 'FAIL', 'error': error_msg, 'traceback': tb}


if __name__ == '__main__':
    # Test with a simple example
    print("Testing run_example:")
    
    # Should pass
    result1 = run_example('x = 5\nprint(x)')
    print(f"  Simple code: {result1}")
    
    # Should fail
    result2 = run_example('1 / 0')
    print(f"  Division by zero: {result2}")
    
    # Should fail
    result3 = run_example('undefined_variable')
    print(f"  Undefined variable: {result3}")
