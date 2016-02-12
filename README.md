# dont-argue
Dead-simple minimal argument parsing in python.

I got sick of wrestling with argparse all the time when all I needed to do was
get a few simple args from the command line. Use this if you just want to get
moving as fast as possible. For more complicated things, use the built in
argparse module.

## Usage

dont_argue supplies a decorator **supply_args** which takes names for command
line arguments and will map those arguments to function arguments of the same
name. For anything more complicated, use argparse instead.
```python
from dont_argue import supply_args

@supply_args('foo', 'bar')
def main(foo, bar):
    print foo, bar
```
