#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# PyTorch documentation build configuration file, created by
# sphinx-quickstart on Fri Dec 23 13:31:47 2016.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
import os
import re
import warnings

import pytorch_sphinx_theme

# -- General configuration ------------------------------------------------

warnings.filterwarnings("ignore", module=r"matplotlib\..*")


# If your documentation needs a minimal Sphinx version, state it here.
#
needs_sphinx = "1.6"

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.doctest",
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
    "sphinx.ext.coverage",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinxcontrib.katex",
    "sphinxcontrib.bibtex",
    "sphinx_gallery.gen_gallery",
]

# katex options
#
#

katex_options = r"""
delimiters : [
   {left: "$$", right: "$$", display: true},
   {left: "\\(", right: "\\)", display: false},
   {left: "\\[", right: "\\]", display: true}
]
"""

bibtex_bibfiles = ["refs.bib"]


def _get_var(var, default=False):
    if var not in os.environ:
        return default

    val = os.environ.get(var, "0")
    trues = ["1", "true", "TRUE", "on", "ON", "yes", "YES"]
    falses = ["0", "false", "FALSE", "off", "OFF", "no", "NO"]
    if val in trues:
        return True
    if val not in falses:
        print(
            f" --- WARNING: Unexpected environment variable value `{var}={val}`. " f"Expected one of {trues + falses}"
        )
    return False


def _get_pattern():
    pattern = os.getenv("GALLERY_PATTERN")
    # If BUILD_GALLERY is falsy -> no build
    # If BUILD_GALLERY is truey -> build
    # If BUILD_GALLERY is undefined
    #    If GALLERY_PATTERN is defined     -> build
    #    If GALLERY_PATTERN is not defined -> not build
    if not _get_var("BUILD_GALLERY", default=False if pattern is None else True):
        if pattern is not None:
            print(
                ' --- WARNING: "GALLERY_PATTERN" is provided, but "BUILD_GALLERY" value is falsy. '
                "Sphinx galleries are not built. To build galleries, set `BUILD_GALLERY=1`."
            )
        return {
            "ignore_pattern": r"\.py",
        }

    ret = {"filename_pattern": "tutorial.py"}
    if os.getenv("GALLERY_PATTERN"):
        # See https://github.com/pytorch/tutorials/blob/cbf2238df0e78d84c15bd94288966d2f4b2e83ae/conf.py#L75-L83
        ret["ignore_pattern"] = r"/(?!" + re.escape(os.getenv("GALLERY_PATTERN")) + r")[^/]+$"
    return ret


sphinx_gallery_conf = {
    "examples_dirs": [
        "../../examples/tutorials",
    ],
    "gallery_dirs": [
        "tutorials",
    ],
    **_get_pattern(),
    "backreferences_dir": "gen_modules/backreferences",
    "first_notebook_cell": None,
    "doc_module": ("torchaudio",),
}
autosummary_generate = True

napoleon_use_ivar = True
napoleon_numpy_docstring = False
napoleon_google_docstring = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = ".rst"

# The master toctree document.
master_doc = "index"

# General information about the project.
project = "Torchaudio"
copyright = "2018, Torchaudio Contributors"
author = "Torchaudio Contributors"

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
# TODO: change to [:2] at v1.0
version = "main "
# The full version, including alpha/beta/rc tags.
# TODO: verify this works as expected
release = "main"

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ["*/index.rst"]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "pytorch_sphinx_theme"
html_theme_path = [pytorch_sphinx_theme.get_html_theme_path()]

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {
    "pytorch_project": "audio",
    "collapse_navigation": False,
    "display_version": True,
    "logo_only": True,
    "navigation_with_keys": True,
    "analytics_id": "UA-117752657-2",
}

html_logo = "_static/img/pytorch-logo-dark.svg"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]
html_css_files = ["https://cdn.jsdelivr.net/npm/katex@0.10.0-beta/dist/katex.min.css", "css/custom.css"]

# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = "TorchAudiodoc"


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',
    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',
    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',
    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, "pytorch.tex", "Torchaudio Documentation", "Torch Contributors", "manual"),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [(master_doc, "Torchaudio", "Torchaudio Documentation", [author], 1)]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        master_doc,
        "Torchaudio",
        "Torchaudio Documentation",
        author,
        "Torchaudio",
        "Load audio files into pytorch tensors.",
        "Miscellaneous",
    ),
]


# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {
    "python": ("https://docs.python.org/3/", None),
    "numpy": ("https://numpy.org/doc/stable/", None),
    "torch": ("https://pytorch.org/docs/stable/", None),
}

# -- A patch that prevents Sphinx from cross-referencing ivar tags -------
# See http://stackoverflow.com/a/41184353/3343043

from docutils import nodes
from sphinx import addnodes
from sphinx.util.docfields import TypedField


def patched_make_field(self, types, domain, items, **kw):
    # `kw` catches `env=None` needed for newer sphinx while maintaining
    #  backwards compatibility when passed along further down!

    # type: (list, str, tuple) -> nodes.field
    def handle_item(fieldarg, content):
        par = nodes.paragraph()
        par += addnodes.literal_strong("", fieldarg)  # Patch: this line added
        # par.extend(self.make_xrefs(self.rolename, domain, fieldarg,
        #                           addnodes.literal_strong))
        if fieldarg in types:
            par += nodes.Text(" (")
            # NOTE: using .pop() here to prevent a single type node to be
            # inserted twice into the doctree, which leads to
            # inconsistencies later when references are resolved
            fieldtype = types.pop(fieldarg)
            if len(fieldtype) == 1 and isinstance(fieldtype[0], nodes.Text):
                typename = "".join(n.astext() for n in fieldtype)
                typename = typename.replace("int", "python:int")
                typename = typename.replace("long", "python:long")
                typename = typename.replace("float", "python:float")
                typename = typename.replace("type", "python:type")
                par.extend(self.make_xrefs(self.typerolename, domain, typename, addnodes.literal_emphasis, **kw))
            else:
                par += fieldtype
            par += nodes.Text(")")
        par += nodes.Text(" -- ")
        par += content
        return par

    fieldname = nodes.field_name("", self.label)
    if len(items) == 1 and self.can_collapse:
        fieldarg, content = items[0]
        bodynode = handle_item(fieldarg, content)
    else:
        bodynode = self.list_type()
        for fieldarg, content in items:
            bodynode += nodes.list_item("", handle_item(fieldarg, content))
    fieldbody = nodes.field_body("", bodynode)
    return nodes.field("", fieldname, fieldbody)


TypedField.make_field = patched_make_field


# Based off of
# https://github.com/sphinx-gallery/sphinx-gallery/blob/5b21962284f865beeaeb79cca50c8c394fa60cba/sphinx_gallery/directives.py#L66-L70
def _has_backref(obj):
    this_dir = os.path.dirname(__file__)
    path = os.path.join(this_dir, "gen_modules", "backreferences", f"{obj}.examples")
    return os.path.isfile(path) and os.path.getsize(path) > 0


# Based off of
# https://github.com/pytorch/vision/blob/5335006be7ef01c9f6cb700fe793d7c645e83e84/docs/source/conf.py#L262
def inject_minigalleries(app, what, name, obj, options, lines):
    if what in ("class", "function") and _has_backref(name):
        lines.append(f"Tutorials using ``{name.split('.')[-1]}``:")
        lines.append(f"    .. minigallery:: {name}")
        lines.append("\n")


def setup(app):
    app.connect("autodoc-process-docstring", inject_minigalleries)
