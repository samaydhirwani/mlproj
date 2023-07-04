
from setuptools import setup,find_packages
  
setup(
    name='MLPROJECT',
    version='0.1',
    description='A sample Python package',
    author='Samay',
    author_email='Samay.dhirwani@gmail.com',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
    ],
)