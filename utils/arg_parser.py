import argparse

__all__ = ('arg_parser')

arg_parser = argparse.ArgumentParser(description='Converts JSON files to HTML files')
arg_parser.add_argument('source', type=str, action='store', help='Source JSON file')
arg_parser.add_argument('--dest', type=str, action='store', help='Output HTML filename', default=None, dest='dest')
