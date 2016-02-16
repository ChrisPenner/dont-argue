import argparse
from inspect import getargspec
from functools import partial

test_args = None

def supply_args(func):
    # Get argnames through introspection
    args, _, _, defaults = getargspec(func)
    parser = argparse.ArgumentParser()
    # Set up empty defaults rather than None
    defaults = defaults or []
    # Keywords match up with the last len(defaults) args
    keyword_names = args[-len(defaults):] if defaults else []
    # use the defaults with the keywords and pack them up
    keywords = {k:v for k,v in zip(keyword_names, defaults)}
    # Use what's left over as regular arguments
    args = args[:-len(keyword_names)] if keywords else args

    # Add basic arguments to argparse
    for arg in args:
        parser.add_argument(arg)

    # add keyword arguments to argparse
    for keyword, value in keywords.iteritems():
        parser.add_argument('--' + keyword, default=value)

    # Extras are unexpected arguments, they'll get splatted out.
    kwargs, extras = parser.parse_known_args(test_args)
    # Convert from 'Namespace' object
    kwargs = vars(kwargs)

    # Get all args as a list to avoid weird keyword/splat conflicts
    combined_args = [kwargs[k] for k in args + keyword_names] + extras
    # Apply the args and return the function.
    return partial(func, *combined_args)
