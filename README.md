# dont-argue
Dead-simple command line arguments for python scripts.

I got sick of re-learning the argparse module every time I just needed to pass
in a few simple command line arguments for a python script. `dont_argue` skips
the boring stuff and lets you get started in a flash.

## Usage

**dont\_argue** provides the decorator **supply\_args**, use it on a function
and that function's arguments will be provided from the command line.

Check it out:
```python
#!/usr/bin/python
from dont_argue import supply_args
@supply_args
def main(name, location, *friends):
    friends = ', '.join(friends)
    print 'Hello {} from {} and your friends {}'.format(name, location, friends)

# Now to kick things off we just call the function, the arguments come from the
# command line, so we don't give any here.
main()
```

Try it out:
```
$ ./example.py Joe Alabama Jake Drake
Hello Joe from Alabama and your friends Jake, Drake
```
If that's all you need, then you're done! Also notice how all the extra
arguments get packed up into `*friends` as expected.

You can also work with command line options by specifying keyword arguments for
your function. They can be specified on the command line using the
`--option=value` or `--option value` syntax.
```python
@supply_args
def main(name, mood='FRIENDLY'):
    if mood == 'FRIENDLY':
        print 'Hello {}! Welcome here!'.format(name)
    elif mood == 'ANGRY':
        print 'Hey {}! Get out of my house!'.format(name)
main()
```

Now we can specify `mood` or not. Also note that providing too few arguments or
using the -h flag will display usage information.
```
$ ./test.py Joe
Hello Joe! Welcome here!
$ ./example.py Joe --mood ANGRY
Hey Joe! Get out of my house!
$ ./example.py -h
usage: example.py [-h] [--mood MOOD] name

positional arguments:
  name

optional arguments:
  -h, --help   show this help message and exit
  --mood MOOD
```

**dont_argue** can't handle keyword arguments that you don't explicitly
specify, so `**kwargs` doesn't tend to work.
