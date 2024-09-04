#!/usr/bin/python3
import dis
import marshal
import types


def get_names(py_path):
    with open(py_path, 'rb') as f:
        f.read(8)
        code = marshal.load(f)
    return extract_names(code)


def extract_names(code):
    if isinstance(code, types.CodeType):
        names = set(code.co_name)
        for const in code.co_consts:
            names.update(extract_names(const))
        return names
    return set()


if __name__ == "__main__":
    names = get_names('/tmp/hideen_4.pyc')
    for name in sorted(name for name in names if not name.startswith("__")):
        print(name)
