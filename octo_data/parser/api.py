from typing import IO, Iterable, Text
from .grammar import foo_file


def parse_text(data: str):
    return foo_file.parse(data)

    # FIXME
    return list(parse_stream(data.splitlines()))


def parse_file(file: IO[Text]):
    return list(parse_stream(file))


def parse_stream(data: Iterable[str]):
    for line in data:
        yield
