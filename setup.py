try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Realize sth like [find] command.(make ex6 stronger)',
    'author': 'Murphian',
    'url': 'XXXXXXXXXX',
    'download_url': 'XXXXXXXXXXXXX',
    'author_email': 'murphianx@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['find'],
    'scripts': [],
    'name': 'ex6'
}

setup(**config)