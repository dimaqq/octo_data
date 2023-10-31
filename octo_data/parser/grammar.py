from parsy import regex, string, eof, seq
from .types import Header, Line26, Line28, Line30, Footer, Block, FooFile

datum = regex(r"[^|\n]+")
bar = string("|")
end = string("\n")
the_end = (end | eof).optional()

line_head = seq(
    _type=string("ZHV") << bar,
    foo1=datum << bar,
    foo2=datum << bar,
    foo3=datum << bar,
    foo4=datum << bar,
    foo5=datum << bar,
    foo6=datum << bar,
    foo7=datum << bar,
    _unused=bar.times(3),
    bar=datum << bar,
).combine_dict(Header)

line26 = seq(
    _type=string("026") << bar,
    foo=datum << bar,
    bar=datum << bar,
).combine_dict(Line26)

line28 = seq(
    _type=string("028") << bar,
    foo=datum << bar,
    bar=datum << bar,
).combine_dict(Line28)

line30 = seq(
    _type=string("030") << bar,
    foo1=datum << bar,
    foo2=datum << bar,
    foo3=datum << bar,
    _unused=bar.times(2),
    bar1=datum << bar,
    bar2=datum << bar,
).combine_dict(Line30)

line_foot = seq(
    _type=string("ZPT") << bar,
    foo1=datum << bar,
    foo2=datum << bar,
    _unused=bar,
    bar1=datum << bar,
    bar2=datum << bar,
).combine_dict(Footer)

block = seq(
    line26=line26 << end,
    line28=line28 << end,
    lines30=(line30 << end).times(1, 2),  # FIXME how many are possible?
).combine_dict(Block)

foo_file = seq(
    header=line_head << end,
    blocks=block.many(),
    footer=line_foot << end,
).combine_dict(FooFile)
