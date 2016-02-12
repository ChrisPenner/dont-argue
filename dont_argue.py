import argparse

class supply_args(object):
    def __init__(self, *keywords, **default_keywords):
        self.keywords = keywords
        self.default_keywords = default_keywords

    def __call__(self, func):
        def wrapper( *args, **kwargs):
            parser = argparse.ArgumentParser()
            # add arguments we're expecting
            for name in self.keywords:
                parser.add_argument(name, nargs='?', default=None)

            # add keyword arguments we're expecting
            for name, default in self.default_keywords.iteritems():
                parser.add_argument('--' + name, default=default, nargs='?')
            known, unknown = parser.parse_known_args()
            known = vars(known)
            # Call func with our args keyword matched.
            func(**known)
        return wrapper
