# Assignment
# Fix the following issues to make the functions pure:

# add_custom_command is mutating an input
# add_format is mutating an input
# save_document is mutating an input
# add_line_break has a side effect (printing to stdout) and no return value

from collections.abc import Callable

default_commands: dict[str, Callable[..., object]] = {}
default_formats: list[str] = ["txt", "md", "html"]
saved_documents: dict[str, str] = {}

# Don't edit above this line


def add_custom_command(
    commands: dict[str, Callable[..., object]],
    new_command: str,
    function: Callable[..., object],
) -> dict[str, Callable[..., object]]:
    commands_cp = commands.copy()
    commands_cp[new_command] = function
    return commands_cp


def add_format(formats: list[str], format: str) -> list[str]:
    formats_cp = formats.copy()
    formats_cp.append(format)
    return formats_cp


def save_document(docs: dict[str, str], file_name: str, doc: str) -> dict[str, str]:
    docs_cp = docs.copy()
    docs_cp[file_name] = doc
    return docs_cp


def add_line_break(line: str) -> None:
    return line + "\n\n"