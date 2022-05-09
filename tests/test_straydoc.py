#!/usr/bin/env python

"""Tests for `straydoc` package."""

import pytest
import straydoc


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_content():
    """Sample pytest test function with the pytest fixture as an argument."""
    ast = straydoc.create_markdown_ast("## test1")
    assert len(ast) == 1
    assert ast[0]['type'] == 'heading'
    assert len(ast[0]['children']) == 1
    assert ast[0]['children'][0]['type'] == 'text'
    assert ast[0]['children'][0]['text'] == 'test1'
    assert ast[0]['level'] == 2
    return None


def test_content2():
    sample_markdown = '''
# *section1*
## subsection1

p1
p1

p2

## subsection2

aaaaaa **bbbb** aaaaa
aaaaaa *cccc* aaaaa

## subsection3

### subsubsection

#### paragraph1
#### paragraph2
#### paragraph3

##### subparagraph

ああああああいいいいいい
ああああああいいい
あ
い

ああああああ


    '''[1:-1]

    ast = straydoc.create_markdown_ast(sample_markdown)
    with open("log.txt", "wt") as text_file:
        text_file.write(str(ast))
    latex = straydoc.to_latex(ast)
    with open("log2.tex", "wt") as text_file:
        text_file.write(str("\n".join(latex)))
