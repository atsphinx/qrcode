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

Directive
=========

.. rst:directive:: qrcode

    This directive inserts "QR code" image created from content part.
    This image is SVG using data URI scheme and output ``img`` element
    with ``html`` (and inherited) builder.

    This inherits from :rst:dir:`image` directive.
    You can set any options of :rst:dir:`image`, but only ``alt`` is
    forced to content itself.

    This has additional options.

    .. rst:directive:option:: qr_version

        This is version number of information capacity that is used size of QR Code symbol.
        It must be between 1 and 40.

    .. rst:directive:option:: qr_error_correction

        This is level of "error correction" to restore if code is broken.
        It must be one of "L", "M", "Q", "H" (ascending ordered of restore level).
