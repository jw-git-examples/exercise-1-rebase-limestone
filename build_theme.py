"""Generate a theme file from palette and config template."""

from __future__ import division
from jinja2 import Template
import sys
import build_palette as builder
import palette_spec as config

palette = builder.Palette(config.name,
                          config.background,
                          config.foreground,
                          config.shades)

values = {"name": palette.name}
values.update(palette.rgb_values())

try:
    template_path = sys.argv[1]
except:
    print("Missing argument: path to the template file")
    sys.exit()

with open(template_path, "r") as f:
    template = Template(f.read())

output_path = palette.slug + "." + template_path\
    .replace("-template", "")\
    .replace(".j2", "")

with open(output_path, "w") as f:
    f.write(template.render(**values))
    print("Output written to {}".format(output_path))
