# dont-argue
Dead-simple minimal argument parsing in python.

I got sick of wrestling with argparse all the time when all I needed to do was
get a few simple args from the command line. Use this if you just want to get
moving as fast as possible. For more complicated things use the built in
argparse module instead.

## Usage

dont_argue provides the decorator **supply_args** which takes names for command
line arguments and will map those arguments to function arguments of the same
name.
```python
# test.py
from dont_argue import supply_args

@supply_args('foo', 'bar')
def main(foo, bar):
    print 'Foo:' foo
    print 'Bar:', bar

main() # Note that we don't supply arguments here
```

Now you can use it.
```
$ python test.py myfoo mybar
Foo: myfoo
Bar: mybar
```

You can also specify keyword arguments (command line options) by specifying
them with a default value. Keyword args are set by using `--keyword=value` or
`--keyword value`.
```python
# We provide the defaults in the decorator, not in main
@supply_args('foo', 'bar', my_key=42, another_key='default value')
def main(foo, bar, my_key, another_key):
    print 'Foo:', foo
    print 'Bar:', bar
    print 'my_key', my_key
    print 'another_key', another_key

main()
```

```
$ python test.py myfoo mybar --another_key Unicorns
Foo: myfoo
Bar: mybar
my_key: 42
another_key: Unicorns
```
You can also abbreviate options so long as it is unambiguous
```
$ python test.py myfoo mybar --a Unicorns
Foo: myfoo
Bar: mybar
my_key 42
another_key Unicorns
```

You can pack up extra options into an 'args' argument if you specify args=True.
Note that you MUST name the argument in your main function 'args'.
```python
# We don't use *args, that's taken care of in the decorator.
@supply_args('foo', 'bar', args=True)
def main(foo, bar, args):
    print 'Foo:', foo
    print 'Bar:', bar
    print 'args:', args

main()
```

```
$ python test.py myfoo mybar one two three
Foo: myfoo
Bar: mybar
args: ['one', 'two', 'three']
```

If no extra args are provided, args will be set to the empty list `[]`.

dont_argue will provide useage information if provided too few arguments or run
with the -h flag.
```
$ python test.py
usage: test.py [-h] [--another_key ANOTHER_KEY] [--my_key MY_KEY] foo bar
test.py: error: too few arguments
```
