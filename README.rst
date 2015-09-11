Gamepad and joystick support for the Jupyter notebook
=====================================================

**This project has been adopted into ipython/ipywidgets (see https://github.com/ipython/ipywidgets/pull/123).**

License
-------

BSD License. Copyright 2015 - Sylvain Corlay

Installation
------------

- Install the Python package

.. code-block:: python

    pip install gamepad

or for a development install:

.. code-block:: python

    git clone https://github.com/SylvainCorlay/gamepad.git
    pip install -e gamepad

- Install and register the notebook extension

.. code-block:: python

    python -m gamepad.install

or for a development install:

.. code-block:: python

    python -m gamepad.install --user --symlink

Usage
-----

See the `example notebook <https://github.com/SylvainCorlay/gamepad/blob/master/examples/demo.ipynb>`_.
