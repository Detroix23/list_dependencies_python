"""
# List Dependencies.
/src/list_dependencies_detroix23/__main__.py
"""

import sys
from typing import Final

from list_dependencies_detroix23 import cli

def main() -> None:
	"""
	Main entry point.
	"""
	print("# List dependencies.\n")

	arguments: Final[list[str]] = sys.argv[1:]

	cli.cli(arguments)

main()
