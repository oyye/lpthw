try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'author': 'Ye Ouyang',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'Email address',
    'version': '0.1',
    'install_requires': ['nose'],
    'pakcages': ['NAME'],
    'scripts': [],
    'name': 'projectname'
}

setup(**config)