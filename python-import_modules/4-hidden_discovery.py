#!/usr/bin/python3
import importlib.util
import sys


def print_module_names(module):
    names = sorted(name for name in dir(module) if not name.startswith("__"))
    for name in names:
        print(name)


if __name__ == "__main__":
    module_name = "hidden_4"
    file_path = "/tmp/hidden_4.pyc"

    spec = importlib.util.spec_from_file_location(module_name, file_path)
    hidden_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(hidden_module)

    print_module_names(hidden_module)
