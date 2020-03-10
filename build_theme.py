"""Generate a theme file from palette and config template."""

from __future__ import division
from jinja2 import Template
import build_palette as builder
import palette_spec as config

palette = builder.Palette(config.name,
                          config.background,
                          config.foreground,
                          config.shades)

values = {"name": palette.name}
values.update(palette.rgb_values())

with open("vscode-template.json.j2", "r") as f:
    template = Template(f.read())

output_path = palette.slug + ".vscode.json"
with open(output_path, "w") as f:
    f.write(template.render(**values))
    print("Output written to {}".format(output_path))
