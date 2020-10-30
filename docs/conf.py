#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# cloud_bids_layout documentation build configuration file, created by
# sphinx-quickstart on Fri Jun  9 13:47:02 2017.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import alabaster
import os
import sys

# General information about the project
project = "Cloud-BIDS-Layout"
copyright = "2020, Adam Richie-Halford"
author = "Adam Richie-Halford"

currentdir = os.path.abspath(os.path.dirname(__file__))

sys.path.append(os.path.join(currentdir, "tools"))

# If extensions (or modules to document with autodoc) are in another
# directory, add these directories to sys.path here. If the directory is
# relative to the documentation root, use os.path.abspath to make it
# absolute, like shown here.
sys.path.insert(0, os.path.abspath(".."))

import cloud_bids_layout

# -- General configuration ---------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
needs_sphinx = "1.0"  # numpydoc requires sphinx >= 1.0

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = ["sphinx.ext.autodoc", "sphinx.ext.viewcode"]
sys.path.append(os.path.abspath("sphinxext"))

extensions = [
    "nbsphinx",
    "sphinx.ext.mathjax",
    "sphinx.ext.autodoc",
    "sphinx.ext.doctest",
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
    "sphinx.ext.coverage",
    "sphinx.ext.ifconfig",
    "sphinx.ext.autosummary",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "alabaster",
]

nbsphinx_allow_errors = False
nbsphinx_execute = "never"

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = ".rst"

# The master toctree document.
master_doc = "index"

# --- Sphinx Gallery ---
sphinx_gallery_conf = {
    # path to your examples scripts
    "examples_dirs": "../examples",
    # path where to save gallery generated examples
    "gallery_dirs": "auto_examples",
    # To auto-generate example sections in the API
    "doc_module": ("cloud_bids_layout",),
    # Auto-generated mini-galleries go here
    "backreferences_dir": "gen_api",
}

# Automatically generate stub pages for API
autoclass_content = "both"  # include both class docstring and __init__
autodoc_default_flags = ["members", "inherited-members"]
autosummary_generate = True

# Napoleon settings (other than default)
napoleon_google_docstring = False
napoleon_use_rtype = False

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = cloud_bids_layout.__version__
# The full version, including alpha/beta/rc tags.
release = cloud_bids_layout.__version__

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output -------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = "alabaster"

# Theme options are theme-specific and customize the look and feel of a
# theme further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {
    "description": "Use pybids with datasets in the cloud",
    "github_user": "nrdg",
    "github_repo": "cloud_bids_layout",
    "github_type": "star",
    "show_powered_by": True,
    "fixed_sidebar": True,
}

# Add any paths that contain custom themes here, relative to this directory.
html_theme_path = [alabaster.get_path()]

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# Custom sidebar templates, maps document names to template names.
html_sidebars = {"**": ["about.html", "navigation.html", "searchbox.html"]}

# If false, no module index is generated.
# html_domain_indices = True
html_domain_indices = False

# -- Options for HTMLHelp output ---------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = "cloud_bids_layoutdoc"


# -- Options for LaTeX output ------------------------------------------

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
# (source start file, target name, title, author, documentclass
# [howto, manual, or own class]).
latex_documents = [
    (
        master_doc,
        "cloud_bids_layout.tex",
        "Cloud-BIDS-Layout Documentation",
        "Adam Richie-Halford",
        "manual",
    )
]


# -- Options for manual page output ------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, "cloud_bids_layout", "Cloud-BIDS-Layout Documentation", [author], 1)
]


# -- Options for Texinfo output ----------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        master_doc,
        "cloud_bids_layout",
        "Cloud-BIDS-Layout Documentation",
        author,
        "cloud_bids_layout",
        "Use pybids with datasets in the cloud.",
        "Miscellaneous",
    )
]