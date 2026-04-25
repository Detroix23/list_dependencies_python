"""
# List Dependencies.
/src/list_dependencies_detroix23/cli.py
"""

import pathlib
from typing import NoReturn

from list_dependencies_detroix23 import definitions, discoverer, dependencies, tests

def incorrect_arguments(message: str) -> NoReturn:
	"""
	Signals to the user an incorrect argument, printing a `message` to the console.

	Prints: "(X) Incorrect arguments: {`message`}. {`USE_STRING`}"
	
	**Exits** Python.
	""" 
	print(f"(X) Incorrect arguments: {message}. {definitions.USE_STRING}")
	exit(1)


def help_cli() -> NoReturn:
	print(definitions.USE_STRING)
	exit(0)

def run_extraction(path: pathlib.Path) -> set[str]:
	"""
	From a `path`, extract all module names. 
	
	Returns, for print purpose: modules: `set[str]`.
	"""
	d = discoverer.Discoverer(
		path,
		files_include_extensions=["py", "pyc", "pyi"],
		folder_exclude_prefixes=["__", "."],
	)

	files: list[pathlib.Path] = d.discover()

	print("Analyzing files: ")
	print(definitions.format_list(list(files)))

	modules: set[str] = dependencies.analyze_project_raw(files)
	print("Modules (built-in included): ")
	print(definitions.format_list(list(modules)))

	return dependencies.filter_modules(modules, definitions.DEFAULT_PYTHON_MODULES)

def cli(arguments: list[str]) -> NoReturn:
	"""
	Launch different function given `arguments`:
	"""
	if len(arguments) < 1:
		incorrect_arguments("not enough.")
	
	if len(arguments) > 1:
		print(f"(!) Ignoring arguments: too many ({len(arguments)}).")

	if arguments[0] == "--test":
		tests.assertions_lines1()
		tests.test_flow1()
		
		exit(0)
	elif arguments[0] in {"-h", "--help"}:
		help_cli()
	else:
		path = pathlib.Path(arguments[0])
		print(list(path.iterdir()))
		print(f"## Extracting modules in: `{path}`: \n")
		
		modules: set[str] = run_extraction(path)

		print("Modules: ")
		print(definitions.format_list(list(modules)))
		
		exit(0)