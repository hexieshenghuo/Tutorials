# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------
from datetime import datetime
import re
import importlib
import inspect
import logging
import os
import sys
import sphinx
import megengine

# -- Project information -----------------------------------------------------

project = 'MegEngine'
copyright = f'2020-{datetime.now().year}, the MegEngine Open Source Team'
author = 'the MegEngine Open Source Team'
version = megengine.__version__
release = version
language = 'zh_CN'

# -- General configuration ---------------------------------------------------

extensions = [
    'nbsphinx',
    'recommonmark',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.doctest',
    'sphinx.ext.extlinks',
    'sphinx.ext.intersphinx',
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
#    'sphinxcontrib.bibtex',
    'sphinx_copybutton'
]

source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}
source_encoding = "utf-8"

master_doc = 'index'
templates_path = ['_templates']
exclude_patterns = [
    '_build', 
    '_drafts', 
    'examples',
    '**/includes/**',
    '**.ipynb_checkpoints'
]

# -- Options for Extensions -------------------------------------------------

# To auto-generate single html pages in `api/` path
autosummary_generate = True

# The path to the JavaScript file to include in the HTML files in order to load MathJax.
mathjax_path = 'https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js'

mathjax_config = {
    'extensions': ['tex2jax.js'],
    'jax': ['input/TeX', 'output/HTML-CSS'],
}

# Useful for refenrece other projects, eg. :py:class:`zipfile.ZipFile`
intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'numpy': ('https://numpy.org/doc/stable/', None),
    'matplotlib': ('https://matplotlib.org/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None)
}

# Can use the alias name as a new role, e.g. :issue:`123`
extlinks = {
    'issue': ('https://github.com/MegEngine/MegEngine/issues/%s', 'Issue #'),
    'pull': ('https://github.com/MegEngine/MegEngine/pull/%s', 'Pull Requset #')
}

# nbsphinx do not use requirejs (breaks bootstrap)
nbsphinx_requirejs_path = ""    

# nbconvert can convert .ipynb files to sphinx outputs
logger = logging.getLogger(__name__)


try:
    import nbconvert
except ImportError:
    logger.warning("nbconvert not installed. Skipping notebooks.")
    exclude_patterns.append("**/*.ipynb")
else:
    try:
        nbconvert.utils.pandoc.get_pandoc_version()
    except nbconvert.utils.pandoc.PandocMissing:
        logger.warning("Pandoc not installed. Skipping notebooks.")
        exclude_patterns.append("**/*.ipynb")

# -- Options for HTML output -------------------------------------------------

html_theme = 'pydata_sphinx_theme'
html_theme_path = ['_themes']
html_theme_options = {
    'search_bar_text': '输入搜索文本...',
    'search_bar_position': 'sidebar',
    'github_url': 'https://github.com/MegEngine/MegEngine',
    'external_links': [
        { 'name': '论坛', 'url': 'https://discuss.megengine.org.cn/'}, 
        { 'name': 'Brain<sup>++</sup>', 'url': 'https://www.brainpp.com/'}
    ],
    'show_toc_level': 2,
    'use_edit_page_button': False,
    'navigation_with_keys': False,
    'show_prev_next': False
}

html_sidebars = {
    '**': ['sidebar-search-bs.html', 'sidebar-nav-bs.html'],
    'index': ['sidebar-search-bs.html', 'announce-sidebar.html']
}

html_logo = "_static/logo/logo.png"
html_favicon = "_static/logo/megengine-48.png"
html_static_path = ['_static']
html_css_files = [
    'css/custom.css'
]

html_search_language = 'zh'

html_context = {
    'github_user': 'MegEngine',
    'github_repo': 'Tutorials',
    'github_version': 'main',
    'doc_path': ''
}
