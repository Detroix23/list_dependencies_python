"""
# List Dependencies.
/src/list_dependencies_detroix23/__main__.py
"""

import pathlib
from typing import Literal

from list_dependencies_detroix23 import definitions, dependencies, discoverer

def main() -> None:
	"""
	Main entry point.
	"""
	print("# List dependencies.\n")

	assertions_lines1()

	test_flow1()

def assert_eq(left: object, right: object) -> Literal[True]:
	"""
	Compare `left` == `right`. Raise an exception, printing the value if are not equal.
	"""
	if left != right:
		raise AssertionError(f"""(A) assert_eq() left != right
- left: {left},
- right: {right}.
""")
	return True

def test_flow1() -> None:

	print("## Test: discoverer.")
	d1 = discoverer.Discoverer(
		pathlib.Path("F:\\Coding\\Python\\list_dependencies"),
		files_include_extensions=["py"],
		folder_exclude_prefixes=["__", "."]
	)

	files1: list[pathlib.Path] = d1.discover()
	print(f"Discovered: {discoverer.format_discovery(files1)}")

	print("## Test: modules.")
	print(dependencies.analyze_line("from pathlib_detroix23 import Path, Hello, Bye,Good,Space "))
	print(dependencies.analyze_line("from pathlib_detroix23 import Path"))
	print(dependencies.analyze_line("import os"))
	print(dependencies.analyze_line("import pathlib as test"))
	print(dependencies.analyze_line("import pathlib, test,test2,test, hello, "))

	print(f"Project `self`: {dependencies.analyze_project(
		files1, 
		definitions.DEFAULT_PYTHON_MODULES
	)}")

def assertions_lines1() -> None:
	print("## Assertions: line 1... ", end="")
	assert_eq(
		dependencies.analyze_line("import os"),
		{"os"}
	)
	assert_eq(
		dependencies.analyze_line("import os, line_project,guess,intro, "),
		{"os", "line_project", "guess", "intro"}
	)
	assert_eq(
		dependencies.analyze_line("from pathlib_detroix23 import Path"),
		{"pathlib_detroix23"}
	)
	assert_eq(
		dependencies.analyze_line("from pathlib_detroix23 import Path, Hello, Bye,Good,Space "),
		{"pathlib_detroix23"}
	)

	print("Passed. Assertions: line 1.")

main()
