# -*- coding: utf-8 -*-
"""Sphinx configuration file."""


import ret

extensions = ["sphinx.ext.autodoc", "sphinx.ext.napoleon"]

source_suffix = [".rst", ".md"]
master_doc = "index"
exclude_patterns = ["ret/testsret/*", "ret/testing/*"]

project = u"RET"

version = ret.__version__

# -- Options for HTML output ---------------------------------------------------

html_theme = "alabaster"
html_title = "RET"
html_logo = "RetLogo.jpg"
html_theme_options = {
    "logo_only": True,
    "display_version": True,
}

################################################################################

html_favicon = "favicon.ico"
