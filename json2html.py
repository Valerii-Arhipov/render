import converters
import inputs
from utils.arg_parser import arg_parser
from utils.file_helper import FileHelper

__all__ = ('convert_code', )


def convert_code():
    args = arg_parser.parse_args()
    source_filename = args.source
    destination_filename = args.dest
    result = inputs.json_file(source_filename, converters.to_html)

    if destination_filename is None:
        print(result)
    else:
        FileHelper.write_to_file(destination_filename, result)
        print(f'OK. JSON File `{source_filename}` converted to `{destination_filename}`')


if __name__ == '__main__':
    convert_code()
