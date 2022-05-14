#!/usr/bin/env python3

from sys import stderr, argv
from pathlib import Path
from shutil import copytree

def assert_args(cond: bool, message: str) -> None:
    if not cond:
        print(f"new_problem.py: {message}", file=stderr)
        exit(-1)

assert_args(len(argv) in range(2, 4), "Expected a template directory to use")

template = Path(argv[1])
template_path = Path("./templates").joinpath(template)

assert_args(template_path.exists(), f"Template directory '{argv[1]}' does not exist")

if len(argv) == 3 and argv[2].isnumeric():
    new_problem = Path(argv[2])
else:
    current_problems = sorted([int(path.name) for path in Path("./problems").iterdir() if path.name.isnumeric()])
    last_consecutive = 1
    for problem in current_problems:
        if last_consecutive == problem:
            last_consecutive += 1
    new_problem = Path(str(last_consecutive))

new_problem_path = Path("./problems").joinpath(new_problem)

assert_args(not new_problem_path.exists(), f"Problem directory '{str(new_problem)}' already exists")

copytree(str(template_path), str(new_problem_path))

print(str(new_problem_path))
