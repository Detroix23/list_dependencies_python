"""
# List Dependencies.
/src/list_dependencies_detroix23/discoverer.py
"""

import pathlib

class Discoverer:
	"""
	# `Discoverer` of files in the project.
	List all required files for treatment in a given `path`.
	"""
	path: pathlib.Path
	files_include_extensions: list[str]
	folder_exclude_prefixes: list[str]

	def __init__(
		self, 
		path: pathlib.Path, 
		files_include_extensions: list[str],
		folder_exclude_prefixes: list[str],
	) -> None:
		"""
		Instantiate the `Discoverer`. To list the files, use `discover()`.
		"""
		self.path = path
		self.files_include_extensions = files_include_extensions
		self.folder_exclude_prefixes = folder_exclude_prefixes

	def is_file_matching(self, path: pathlib.Path) -> bool:
		"""
		Return if the file at `path` respects the name criteria.
		""" 
		suffix: str = path.suffix[1:]
		return suffix in self.files_include_extensions

	def is_directory_matching(self, path: pathlib.Path) -> bool:
		"""
		Return if the directory at `path` respects the name criteria.
		""" 
		for prefix in self.folder_exclude_prefixes:
			if path.name.startswith(prefix):
				return False

		return True

	def discover(self) -> list[pathlib.Path]:
		"""
		Return a list of files matching the requirements.
		"""
		path: pathlib.Path = self.path

		def discover_recurse(path: pathlib.Path) -> list[pathlib.Path]:
			validated: list[pathlib.Path] = []

			if path.is_file():
				if self.is_file_matching(path):
					validated = [path]
			
			elif path.is_dir():
				if self.is_directory_matching(path):		
					for item in path.iterdir():
						validated += discover_recurse(item)

			return validated

		return discover_recurse(path)

def format_discovery(paths: list[pathlib.Path]) -> str:
	"""
	Return a formatted `[`list`]`: one path per line, starting with a `tab`.
	"""
	return f"[\n\t{'\n\t'.join([str(path) for path in paths])}\n]"
