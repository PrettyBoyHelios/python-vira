from setuptools import setup, find_packages

setup(
    name='python-vira',
    version='0.1',
    description='A library for consuming Vira API services in Python 3.10',
    author='Luis Correa',
    packages=find_packages(),
    install_requires=[
        'requests',
        'python-dotenv'
    ],
)
