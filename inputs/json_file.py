import json
from collections import OrderedDict


def json_file(filename, converter):
    with open(filename, 'r') as file:
        raw = json.load(
            file,
            object_pairs_hook=OrderedDict  # to insure that order of items in json won't be broken
        )

    return converter(raw)
