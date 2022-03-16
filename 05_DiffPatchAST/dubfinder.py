import ast
import difflib
from importlib import import_module
import inspect
import sys
import textwrap

DUBRATIO = 0.95


def get_members(obj, module):
    prepared = {}
    all_members = inspect.getmembers(obj)

    for name, member in all_members:
        if inspect.isclass(member):
            if not name.startswith("__"):
                prepared.update(get_members(obj=member, module=f"{module}.{name}"))
        elif inspect.isfunction(member):
            src = inspect.getsource(member)

            if "." in module:
                src = textwrap.dedent(src)

            tree = ast.parse(src)

            for node in ast.walk(tree):
                for attribute in ["name", "id", "arg", "attr"]:
                    if hasattr(node, attribute):
                        setattr(node, attribute, "_")

            prepared_text = ast.unparse(tree)
            prepared.update({f"{module}.{name}": prepared_text})
    return prepared


if __name__ == "__main__":
    members = {}
    for i in range(1, len(sys.argv)):
        module = sys.argv[i]
        obj = import_module(module)
        members.update(get_members(obj, module))

    members_names = sorted(members.keys())

    for i, foo_1 in enumerate(members.keys()):
        for foo_2 in members_names[i + 1 :]:
            if (
                difflib.SequenceMatcher(None, members[foo_1], members[foo_2]).ratio()
                > DUBRATIO
            ):
                print(foo_1, ":", foo_2)
