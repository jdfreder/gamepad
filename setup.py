# -*- coding: utf-8 -*-

try:
    from setuptools import setup
    from setuptools.command.install import install
except ImportError:
    from distutils.core import setup
    from distutils.core.command.install import install


setup(
    name='gamepad',
    version='0.1.1',
    description='Gamepad and Joystick support for the Jupyter notebook.',
    author='Sylvain Corlay',
    author_email='sylvain.corlay@gmail.com',
    license='New BSD License',
    url='https://github.com/SylvainCorlay/gamepad',
    keywords='gamepad joystick simulator flight game python ipython widgets widget',
    classifiers=['Development Status :: 4 - Beta',
                 'Programming Language :: Python'],
    packages=['gamepad'],
)
