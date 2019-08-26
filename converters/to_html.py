import re
import html
from collections import OrderedDict

tag_props_pattern = re.compile('(?P<type>[.#]|^)(?P<name>.+?)(?=[.#]|$)')


def get_tag_props(tag):
    tag_name = ''
    tag_id = None
    tag_classes = []
    for start, name in tag_props_pattern.findall(html.escape(tag)):
        if start == '.':
            tag_classes.append(name)
        elif start == '#' and not tag_id:
            tag_id = name
        else:
            tag_name = name

    tag_with_attr = tag_name

    if tag_id:
        tag_with_attr = f'{tag_with_attr} id="{tag_id}"'

    if len(tag_classes) > 0:
        tag_with_attr = f'{tag_with_attr} class="{" ".join(tag_classes)}"'

    return tag_with_attr, tag_name


def get_tag_content(content):
    if isinstance(content, OrderedDict):
        raise TypeError('Tag content can\'t be instance of Dict')

    if isinstance(content, list):
        return to_html(content)

    return html.escape(str(content))


def to_tag(item, tag):
    tag_open, tag_close = get_tag_props(tag)
    return f'<{tag_open}>{get_tag_content(item[tag])}</{tag_close}>'


def to_html(tree):
    if not isinstance(tree, list):
        raise TypeError(f'Expected type {type(list())}. Got {type(tree)}')

    result = ''
    for item in tree:
        tags = ''
        for tag in item:
            tags = f'{tags}{to_tag(item, tag)}'

        result = f'{result}<li>{tags}</li>'

    return f'<ul>{result}</ul>'
