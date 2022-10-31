from setuptools import setup
from setuptools import find_packages

# Package meta-data.
setup(
    name = 'Kakan',
    description = 'machine learning lib and something else',
    url = 'https://github.com/Kakanom/Machine-learning',
    email = 'frostikoil@gmail.com',
    author = 'Kakanom',
    requires_python = '>=3.6.0',
    version = '1.0.1',
    install_requires = ['numpy>=1.20.3',
                        'matplotlib>=3.4.3',
                        'pandas>=1.3.4',
                        'scikit_learn>=1.0.2'],
    packages = find_packages(),
    entry_points = {
        'console_scripts':[
            'src-cli = src.main:main'
        ],
    },
)