from octo_data.parser import parse_text
from octo_data.parser.grammar import (
    line26,
    line28,
    line30,
    block,
    foo_file,
    line_head,
    line_foot,
)
from octo_data.parser.types import Line26, Line28, Line30


def test_26():
    assert line26.parse("026|a|b|") == Line26("a", "b")


def test_28():
    assert line28.parse("028|a|b|") == Line28("a", "b")


def test_30():
    assert line30.parse("030|D|2|8|||T|N|") == Line30("D", "2", "8", "T", "N")


def test_block(sample):
    a, b, c = sample("026"), sample("028"), sample("030")
    assert block.parse(f"{a}\n{b}\n{c}\n")
    assert block.parse(f"{a}\n{b}\n{c}\n{c}\n")


def test_header(sample):
    assert line_head.parse(sample("ZHV"))


def test_footer(sample):
    assert line_foot.parse(sample("ZPT"))


def test_file(sample):
    a, b = sample("ZHV"), sample("ZPT")
    assert foo_file.parse(f"{a}\n{b}\n")
    # assert foo_file.parse(f"{a}\n{b}")


def test_smoke(sample_data):
    afile = parse_text(sample_data)
    assert afile.header
    assert afile.header.bar == "OPER"
    assert afile.footer
    assert afile.footer.bar1 == "11"
    assert len(afile.blocks) == 11
    assert [len(b.lines30) for b in afile.blocks] == [1, 1, 1, 1, 1, 2, 1, 1, 1, 2, 1]
