# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'bigdata-car'
copyright = '2023, jklee2'
author = 'jklee2'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# extensions = []

templates_path = ['_templates']
exclude_patterns = []

extensions = ['sphinx.ext.autodoc', 'myst_parser']
html_theme = 'sphinx_rtd_theme'

source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = 'alabaster'
html_static_path = ['_static']
html_logo = "_static/KADaP_Only.png"
html_theme_options = {
    "logo_only": True,
    "display_version": False,
}

import os
import sys
sys.path.insert(0, os.path.abspath('../../src'))
