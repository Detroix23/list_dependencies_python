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
	found: list[pathlib.Path]
	files_include_extensions: list[str]
	""" Allowed file extensions. Do **not** include the dot."""
	folder_exclude_prefixes: list[str]

	def __init__(
		self, 
		path: pathlib.Path, 
		files_include_extensions: list[str],
		folder_exclude_prefixes: list[str],
	) -> None:
		"""
		Instantiate the `Discoverer`. To list the files, use `discover()`.

		Arguments:
		- `files_include_extensions`: do **not** include the dot in the extension.
		"""
		self.path = path
		self.found = []
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

		discovered: list[pathlib.Path] = discover_recurse(path)
		self.found += discovered
		return discovered
