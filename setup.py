from distutils.core import setup

with open('README.md') as f:
    long_description = f.read()

version = '0.1.3'

setup(
    name = 'dont_argue',
    packages = ['dont_argue'],
    package_data={ 'dont_argue': ['README.md'], },
    version = version,
    description = 'Dead-simple command line argument parsing',
    long_description=long_description,
    author = 'Chris Penner',
    author_email = 'christopher.penner@gmail.com',
    url = 'https://github.com/ChrisPenner/dont-argue',
    download_url = 'https://github.com/ChrisPenner/dont-argue/releases/tag/v{}'.format(version), 
    license = 'MIT',
    keywords = ['command line', 'argument', 'parsing', 'argparse'],
    classifiers = [
        'Development Status :: 3 - Alpha',

        'Topic :: Software Development :: Libraries',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],
)
