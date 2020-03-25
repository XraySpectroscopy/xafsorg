# -*- coding: utf-8 -*-
#

import sphinx_rtd_theme

project = 'xafs.org'
copyright = 'Public Domain. See About for Auhtors'
release = '0.1'
html_title = 'XAFS.ORG'
html_short_title = 'XAFS.ORG'

pygments_style = 'sphinx'
html_theme = 'sphinx_rtd_theme'

extensions = ['sphinx.ext.todo', 'sphinx.ext.mathjax',
              "sphinx_rtd_theme"]

intersphinx_mapping = {'py': ('https://docs.python.org/3/', None)}

templates_path = ['_templates']
source_suffix = '.rst'
source_encoding = 'utf-8'

master_doc = 'index'

exclude_trees = ['_build']

add_function_parentheses = True
add_module_names = False

html_static_path = ['_static']

html_sidebars = {'index': ['indexsidebar.html','searchbox.html']}
html_show_sourcelink = True
