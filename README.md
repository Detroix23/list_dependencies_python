# List dependencies.
Sometimes, files `requirements.txt` or `pyproject.toml` are not complete in their external modules
definition.

This scripts allow to list all required modules to run a project, filtering built-in libraries.

I made this because I can forgot, a lot, to write these files. Are custom made:
- the file discoverer;
- the dependencies parser.

## The command-line tool.
Execute the script entry-point: 
```bash
py src/list_dependencies_detroix23/__main__.py <path>
```

Arguments:
- `--help` | `-h`: print helpful message and exists.
- `--test`: execute the tests bundled in the script.
- `<path>`: the path to project to analyze.

Can be used shorter scripts:
- see: [Scripts](https://github.com/Detroix23/Scripts)
