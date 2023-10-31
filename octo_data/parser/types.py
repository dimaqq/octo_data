from pydantic.dataclasses import dataclass


@dataclass
class Header:
    foo1: str
    foo2: str
    foo3: str
    foo4: str
    foo5: str
    foo6: str
    foo7: str
    bar: str


@dataclass
class Footer:
    foo1: str
    foo2: str
    bar1: str
    bar2: str


@dataclass
class Line26:
    foo: str
    bar: str


@dataclass
class Line28:
    foo: str
    bar: str


@dataclass
class Line30:
    foo1: str
    foo2: str
    foo3: str
    bar1: str
    bar2: str


@dataclass
class Block:
    line26: Line26
    line28: Line28
    lines30: list[Line30]


@dataclass
class FooFile:
    header: Header
    blocks: list[Block]
    footer: Footer
