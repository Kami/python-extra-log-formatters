import os
import sys

from setuptools import setup


def read_version_string():
    version = None
    current_dir = os.path.abspath(os.path.dirname(__file__))
    sys.path.insert(0, current_dir)
    from log_formatters import __version__
    version = __version__
    sys.path.pop(0)
    return version


setup(
    name='log-formatters',
    version=read_version_string(),
    #long_description=open('README.rst').read() + '\n\n' +
    #open('CHANGES.rst').read(),
    packages=[
        'log_formatters'
    ],
    package_dir={
        'log_formatters': 'log_formatters'
    },
    url='https://github.com/Kami/python-log-formatters/',
    license='Apache License (2.0)',
    author='Tomaz Muraus',
    author_email='tomaz+pypi@tomaz.me',
    description='A collection of useful Python log formatter classes.',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
