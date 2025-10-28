"""
Parser for extracting doctest examples from Python docstrings.
"""
import ast
from pathlib import Path
from typing import List, Dict, Optional


def get_doctest_examples(file_path: Path) -> List[Dict]:
    """
    Extract all doctest examples (>>> lines) from a Python file's docstrings.
    
    Args:
        file_path: Path to Python file to parse
    
    Returns:
        List of dicts containing example metadata and code
    
    Example:
        >>> # This would find examples in a real file
        >>> examples = get_doctest_examples(Path('scanner.py'))
        >>> isinstance(examples, list)
        True
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            source = f.read()
    except (UnicodeDecodeError, FileNotFoundError):
        return []
    
    try:
        tree = ast.parse(source, filename=str(file_path))
    except SyntaxError:
        # Skip files with syntax errors
        return []
    
    examples = []
    
    # Only check nodes that can have docstrings
    for node in ast.walk(tree):
        if not isinstance(node, (ast.FunctionDef, ast.ClassDef, ast.Module, ast.AsyncFunctionDef)):
            continue
            
        docstring = ast.get_docstring(node)
        if docstring and '>>>' in docstring:
            # Extract the node name
            node_name = _get_node_name(node)
            
            # Parse out the code from doctest format
            code = _extract_doctest_code(docstring)
            
            if code:
                examples.append({
                    'file': file_path,
                    'location': node_name,
                    'line': node.lineno if hasattr(node, 'lineno') else 0,
                    'code': code,
                    'raw_docstring': docstring
                })
    
    return examples


def _get_node_name(node) -> str:
    """Get a human-readable name for an AST node."""
    if isinstance(node, ast.FunctionDef):
        return f"function '{node.name}'"
    elif isinstance(node, ast.ClassDef):
        return f"class '{node.name}'"
    elif isinstance(node, ast.Module):
        return "module docstring"
    else:
        return f"{type(node).__name__}"


def _extract_doctest_code(docstring: str) -> Optional[str]:
    """
    Extract executable Python code from doctest format.
    
    Converts:
        >>> x = 5
        >>> print(x)
        5
    
    To:
        x = 5
        print(x)
    
    (Note: We ignore expected output lines for now)
    """
    lines = docstring.split('\n')
    code_lines = []
    
    for line in lines:
        stripped = line.strip()
        if stripped.startswith('>>>'):
            # Remove '>>> ' prefix
            code_lines.append(stripped[4:])
        elif stripped.startswith('...'):
            # Continuation line, remove '... ' prefix
            code_lines.append(stripped[4:])
        # Skip expected output lines (lines that don't start with >>> or ...)
    
    code = '\n'.join(code_lines)
    return code if code.strip() else None


if __name__ == '__main__':
    # Quick test on this file itself
    examples = get_doctest_examples(Path(__file__))
    print(f"Found {len(examples)} doctest examples in this file:")
    for ex in examples:
        print(f"\n  Location: {ex['location']}")
        print(f"  Code:\n{ex['code']}")
