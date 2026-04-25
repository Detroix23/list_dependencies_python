"""
# List Dependencies.
/src/list_dependencies_detroix23/dependencies.py
"""

import pathlib
import re

def analyze_line(line: str) -> set[str]:
	"""
	Return all modules found in `line`.
	"""
	FORBIDDEN: set[str] = {".", " ", ",", ";", "(", ")"}
	tokens: list[str] = re.split(r"[,\s]", line.strip())
	modules: set[str] = set()

	if tokens[0] == "import":
		i: int = 1
		pure_imports: bool = True
		while pure_imports and i < len(tokens):
			if tokens[i] == "as":
				pure_imports = False
			elif tokens[i] and set(tokens[i]).isdisjoint(FORBIDDEN):
				modules.add(tokens[i])
			
			i += 1
	
	elif (
		tokens[0] == "from" 
		and len(tokens) >= 4 
		and tokens[2] == "import"
		and set(tokens[1]).isdisjoint(FORBIDDEN)
	):
		modules.add(tokens[1])
	
	return modules

def analyze_file(path: pathlib.Path) -> set[str]:
		"""
		Open a file `path`, and returns the name of the used modules.

		Looks `module` in syntax structures, only at the begging of the line:
		- `import <module>`;
		- `from <module> import ...`;
		"""
		modules: set[str] = set()

		with open(path, 'r') as code:
			for line in code.readlines():
				modules |= analyze_line(line.strip())
		
		return modules

def analyze_project_raw(
	paths: list[pathlib.Path],
) -> set[str]:
	"""
	Return the conglomerate of modules found in project `path` as a `list[str]`.
	"""
	modules: set[str] = set()
	for path in paths:
		modules_file: set[str] = analyze_file(path)
		modules |= modules_file
	
	return modules

def filter_modules(modules: set[str], filterer: set[str]) -> set[str]:
	"""
	Use `set` operation subtraction to remove from `modules` any of `filter`.  
	"""
	return modules - filterer

def analyze_project(
	paths: list[pathlib.Path],
	exclude: set[str]
) -> set[str]:
	"""
	Return the conglomerate of modules found in project `path` as a `list[str]`.
	"""
	modules: set[str] = set()
	for path in paths:
		modules_file: set[str] = analyze_file(path)
		modules |= modules_file
	
	return filter_modules(modules, exclude)