"""
# List Dependencies.
/src/list_dependencies_detroix23/__main__.py
"""

import pathlib

from list_dependencies_detroix23 import discoverer

def main() -> None:
	"""
	Main entry point.
	"""
	d1 = discoverer.Discoverer(
		pathlib.Path("F:\\Coding\\Python\\list_dependencies"),
		files_include_extensions=["py"],
		folder_exclude_prefixes=["__", "."]
	)

	print(f"Discovered: {discoverer.format_discovery(d1.discover())}")

main()
