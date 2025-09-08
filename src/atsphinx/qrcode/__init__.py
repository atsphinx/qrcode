"""Render QRCode image on Sphinx document."""

from __future__ import annotations

import base64
from typing import TYPE_CHECKING

from docutils.parsers.rst.directives.images import Image

if TYPE_CHECKING:
    from sphinx.application import Sphinx

__version__ = "0.0.0"


class QRodeDirective(Image):  # noqa: D101
    required_arguments = 0
    option_spec = Image.option_spec | {}  # type: ignore[unsupported-operator]
    has_content = True

    def run(self):  # noqa: D102
        # NOTE: This is third-party library.
        import qrcode
        import qrcode.image.svg

        content = "\n".join(self.content)
        svg = qrcode.make(content, image_factory=qrcode.image.svg.SvgPathImage)
        data = base64.b64encode(svg.to_string()).decode()
        self.arguments = [f"data:image/svg+xml;base64,{data}"]
        self.options["alt"] = content.replace("\n", " ")
        return super().run()


def setup(app: Sphinx):  # noqa: D103
    app.add_directive("qrcode", QRodeDirective)
    return {
        "version": __version__,
        "env_version": 1,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
