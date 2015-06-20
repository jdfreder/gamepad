# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name='gamepad',
    version='0.1.5',
    description='Gamepad and Joystick support for the Jupyter notebook.',
    author='Sylvain Corlay',
    author_email='sylvain.corlay@gmail.com',
    license='New BSD License',
    url='https://github.com/SylvainCorlay/gamepad',
    packages=['gamepad'],
    include_package_data=True,
    keywords='gamepad joystick simulator flight game python ipython widgets widget',
    classifiers=['Development Status :: 4 - Beta',
                 'Programming Language :: Python'],
)
