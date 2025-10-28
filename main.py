"""
DocTest Checker - Validate code examples in Python docstrings.

Usage:
    python main.py [directory]
    
If no directory is specified, uses current directory.
"""
import sys
from pathlib import Path
from scanner import find_python_files
from parser import get_doctest_examples
from runner import run_example


def main(directory: str = '.'):
    """
    Main function to scan, parse, and test docstring examples.
    
    Args:
        directory: Root directory to scan for Python files
    """
    print("="*60)
    print("DocTest Checker - Validating Code Examples")
    print("="*60)
    print(f"\nScanning directory: {Path(directory).resolve()}\n")
    
    # Step 1: Find all Python files
    files = find_python_files(directory)
    print(f"Found {len(files)} Python file(s)")
    
    # Step 2: Extract all doctest examples
    all_examples = []
    for file in files:
        examples = get_doctest_examples(file)
        all_examples.extend(examples)
    
    print(f"Found {len(all_examples)} doctest example(s)\n")
    
    if len(all_examples) == 0:
        print("No doctest examples found. Add some using >>> syntax in docstrings!")
        return
    
    print("="*60)
    print("Running Tests...")
    print("="*60 + "\n")
    
    # Step 3: Run each example and collect results
    results = []
    for example in all_examples:
        result = run_example(example['code'])
        results.append({
            'example': example,
            'result': result
        })
    
    # Step 4: Generate report
    passed = sum(1 for r in results if r['result']['status'] == 'PASS')
    failed = sum(1 for r in results if r['result']['status'] == 'FAIL')
    
    # Show failures first
    if failed > 0:
        print("FAILED EXAMPLES:\n")
        for r in results:
            if r['result']['status'] == 'FAIL':
                ex = r['example']
                print(f"  File: {ex['file']}")
                print(f"  Location: {ex['location']} (line {ex['line']})")
                print(f"  Error: {r['result']['error']}")
                print(f"  Code:")
                for line in ex['code'].split('\n'):
                    print(f"    {line}")
                print()
    
    # Summary
    print("="*60)
    print("SUMMARY")
    print("="*60)
    print(f"Total Examples: {len(results)}")
    print(f"✓ Passed: {passed}")
    print(f"✗ Failed: {failed}")
    print("="*60)
    
    # Exit with error code if any tests failed
    if failed > 0:
        sys.exit(1)
    else:
        print("\n🎉 All doctest examples passed!")
        sys.exit(0)


if __name__ == '__main__':
    # Get directory from command line or use current directory
    directory = sys.argv[1] if len(sys.argv) > 1 else '.'
    main(directory)
