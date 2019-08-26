
# HTML Renderer

Renderer HTML from JSON files


## Requirements

For using converver you have to use `Python 3.6` or higher


### Usage
usage: json2html.py [-h] [--dest DEST] source

positional arguments:
  source       Source JSON file

optional arguments:
  -h, --help   show help message and exit
  --dest Output HTML filename

Example:

```
$ python3 json2html.py source.json --dest result.html
```

To get output to `stdout`
```
$ python3 json2html.py source.json
```

### Testing
```
python3 -m unittest converters/tests/to_html.py 
```
