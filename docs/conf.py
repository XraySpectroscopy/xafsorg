# -*- coding: utf-8 -*-
#

import os, sys, sphinx_rtd_theme

project = 'xrayabsorption.org'
copyright = 'Public Domain. See About for Auhtors'
release = '0.1'
html_title = 'xrayabsorption.org'
html_short_title = 'xrayabsorption.org'

pygments_style = 'sphinx'
html_theme = 'sphinx_rtd_theme'

sys.path.insert(0, os.path.abspath(os.path.join('.', 'ext')))
extensions = ['sphinx.ext.todo', 'sphinx.ext.mathjax',
              "sphinx_rtd_theme", 'subfig',
              ]

intersphinx_mapping = {'py': ('https://docs.python.org/3/', None)}

templates_path = ['_templates']
source_suffix = '.rst'
source_encoding = 'utf-8'

master_doc = 'index'

exclude_trees = ['_build']

add_function_parentheses = True
add_module_names = False

html_static_path = ['_static']
html_favicon = '_static/ixas_logo.ico'

html_sidebars = {'index': ['indexsidebar.html','searchbox.html']}
html_show_sourcelink = True

todo_include_todos = True

