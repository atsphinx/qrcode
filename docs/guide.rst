==========
User guide
==========

Installation
============

.. code-block:: console

    pip install atsphinx-qrcode

Usage
=====

Setup
-----

.. code-block:: python
    :caption: conf.py

    extensions = [
        "atsphinx.qrcode",
    ]

Write into your document
------------------------

.. code-block:: rst

    .. qrcode::

        https://example.com

Configuration
=============

.. todo:: Write after if it requires
