"""Render QRCode image on Sphinx document."""

from __future__ import annotations

import base64
from typing import TYPE_CHECKING

from docutils import nodes
from sphinx.util.docutils import SphinxDirective

if TYPE_CHECKING:
    from sphinx.application import Sphinx

__version__ = "0.0.0"


class QRodeDirective(SphinxDirective):  # noqa: D101
    has_content = True

    def run(self):  # noqa: D102
        # NOTE: This is third-party library.
        import qrcode
        import qrcode.image.svg

        content = "\n".join(self.content)
        svg = qrcode.make(content, image_factory=qrcode.image.svg.SvgPathImage)
        data = base64.b64encode(svg.to_string()).decode()
        image = nodes.image(
            alt=content.replace("\n", " "),
            uri=f"data:image/svg+xml;base64,{data}",
        )
        return [image]


def setup(app: Sphinx):  # noqa: D103
    app.add_directive("qrcode", QRodeDirective)
    return {
        "version": __version__,
        "env_version": 1,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
