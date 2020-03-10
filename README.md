Git rebase exercise
===================

This is an artificial repository for practicing history rewriting. It is based
on real history from https://github.com/jan-warchol/limestone-colors.


Minimalistic syntax highlighting
--------------------------------

This is an attempt to design a syntax highlighting theme that uses only shades
of one or two colors, but still maintains high readability. It's currently in
early phase of development, no stable version has been released yet. **See
[`devel`](https://github.com/jan-warchol/monochrome-syntax/tree/devel) branch
for current state of work.**


Features
--------

- moderate contrast: very readable but not tiring to the eyes
- styling rules designed to make important information easy to find
- precise lightness relationships calculated using CIE Lab colorspace
- parameterized: adjust foreground, background or contrast
  and generate all other shades from that


Theme builder usage
-------------------

First install dependencies:

    pip3 install --user -r requirements.txt

Building a palette:

    python3 build_palette.py

Generating a config file from a template:

    python3 build_theme.py vscode-template.json.j2
