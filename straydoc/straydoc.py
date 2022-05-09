"""Main module."""

import mistune


def create_markdown_ast(markdown_text: str):
    return mistune.create_markdown(renderer='ast')(markdown_text)


def _to_latex(ast: list[any]):
    latex_text = []
    for node in ast:
        if node['type'] == 'text':
            latex_text.append(node['text'])
        elif node['type'] == 'emphasis':
            sub_text = _to_latex(node['children'])
            sub_text.insert(0, '\\emph{')
            sub_text.append('}')
            latex_text.append(''.join(sub_text))
        elif node['type'] == 'strong':
            sub_text = _to_latex(node['children'])
            sub_text.insert(0, '\\textgt{')
            sub_text.append('}')
            latex_text.append(''.join(sub_text))
        elif node['type'] == 'paragraph':
            sub_text = _to_latex(node['children'])
            sub_text.append('\n')
            latex_text.append(''.join(sub_text))
        elif node['type'] == 'heading':
            sub_text = _to_latex(node['children'])
            if node['level'] == 1:
                command = '\\section'
            elif node['level'] == 2:
                command = '\\subsection'
            elif node['level'] == 3:
                command = '\\subsubsection'
            elif node['level'] == 4:
                command = '\\paragraph'
            elif node['level'] == 5:
                command = '\\subparagraph'
            sub_text.insert(0, f'{command}{{')
            sub_text.append('}')
            latex_text.append(''.join(sub_text))
    return latex_text


def to_latex(ast: list[any]):
    latex_text = _to_latex(ast)
    latex_text.insert(0, '\\documentclass{jsarticle}\n\\begin{document}')
    latex_text.append('\\end{document}')
    return latex_text
