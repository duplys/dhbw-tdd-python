from setuptools import setup, find_packages

setup(
    name='my_package',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[],
    author='Paul Duplys',
    author_email='paul.duplys@gmail.com',
    description='Python package skeleton for Test-Driven Development (TDD)',
    url='https://github.com/duplys/dhbw-tdd-python',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Apache 2.0 License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
