"""
# List Dependencies.
/src/list_dependencies_detroix23/definitions.py
"""

import sys
from typing import Final, Sequence

DEFAULT_PYTHON_MODULES: Final[set[str]] = set(sys.stdlib_module_names)

USE_STRING: Final[str] = """
List dependencies: Python.

Usage:
```bash
list_dependencies <path>
```
"""
""" General short and concise help. """

def format_list(paths: Sequence[object], separator: str = "\n  ") -> str:
	"""
	Return a formatted `[`list`]`: one path per line, starting with a `tab`.
	"""
	if len(paths) == 0:
		return "[]"
	return f"[{separator}{separator.join([str(path) for path in paths])}\n]"
