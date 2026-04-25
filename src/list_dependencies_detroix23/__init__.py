# type: ignore
"""
# List Dependencies.
/src/list_dependencies_detroix23/__init__.py

List modules required to run a Python project, in case `pyproject.toml` or `requirements.txt`
may not be correctly written.

Use the command-line interface with:
```bash
python src/list_dependencies_detroix23/__main__.py <path>
```
"""

from . import (
	definitions,
	discoverer,
	dependencies,
)
