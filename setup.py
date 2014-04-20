# -*- encoding:utf-8 -*-
from setuptools import setup, find_packages

setup(
    name='pass-manager',
    version='0.1.2',
    author='petitviolet',
    author_email='violethero0820@gmail.com',
    packages=find_packages(),
    install_requires=[],
    description = 'Simple CLI Password Manager',
    license = 'MIT',
    # scripts = ['src/pass_manager.py'],
    platforms = ['POSIX', 'Windows', 'Mac OS X'],
    entry_points={
        'console_scripts': 'pass-manager = src.pass_manager:main'
    },
    zip_safe=False,
    classifiers=[
          'Environment :: Console',
          'Intended Audience :: Developers',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Topic :: Utilities'
    ]
)
