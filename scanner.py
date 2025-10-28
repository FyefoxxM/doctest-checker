"""
File scanner for finding Python files in a directory.
"""
from pathlib import Path
from typing import List


def find_python_files(directory: str, exclude_dirs: List[str] = None) -> List[Path]:
    """
    Find all Python files in a directory, excluding common non-source directories.
    
    Args:
        directory: Root directory to search
        exclude_dirs: List of directory names to exclude (default: venv, .venv, __pycache__)
    
    Returns:
        List of Path objects pointing to Python files
    
    Example:
        >>> files = find_python_files('.')
        >>> all(f.suffix == '.py' for f in files)
        True
    """
    if exclude_dirs is None:
        exclude_dirs = ['venv', '.venv', '__pycache__', '.git', 'node_modules', 'build', 'dist']
    
    root = Path(directory)
    python_files = []
    
    # If it's a single file, just return that
    if root.is_file() and root.suffix == '.py':
        return [root]
    
    # Otherwise scan directory
    for file in root.rglob('*.py'):
        # Check if any excluded directory is in the file's path
        if not any(excluded in file.parts for excluded in exclude_dirs):
            python_files.append(file)
    
    return python_files


if __name__ == '__main__':
    # Quick test
    files = find_python_files('.')
    print(f"Found {len(files)} Python files:")
    for f in files:
        print(f"  {f}")
