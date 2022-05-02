#!/usr/bin/env python3

from sys import stderr, argv
from pathlib import Path
from shutil import copytree

def assert_args(cond: bool, message: str) -> None:
    if not cond:
        print(f"new_problem.py: {message}", file=stderr)
        exit(-1)

assert_args(len(argv) == 2, "Expected a template directory to use")

template = Path(argv[1])
template_path = Path("./templates").joinpath(template)

assert_args(template_path.exists(), f"Template directory '{argv[1]}' does not exist")

last_problem = max([int(path.name) for path in Path("./problems").iterdir() if path.name.isnumeric()], default=0)
new_problem = Path(str(last_problem + 1))
new_problem_path = Path("./problems").joinpath(new_problem)

copytree(str(template_path), str(new_problem_path))

print(str(new_problem_path))
