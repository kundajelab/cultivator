
from setuptools import setup

setup(
    name='cultivator',
    version='0.0.0',
    author='Jacob Schreiber',
    author_email='jmschreiber91@gmail.com',
    packages=['cultivator'],
    url='http://pypi.python.org/pypi/cultivator/',
    license='LICENSE.txt',
    description='A tool for generating covariate-matched and diversity-maximizing subsets. Generally useful, for built with genomic applications in mind.',
    install_requires=[
        "numpy >= 1.14.2"
    ],
)