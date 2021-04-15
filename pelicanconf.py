#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

AUTHOR = 'Mark Mulligan'
SITENAME = 'MarkLog'
SITEURL = ''  # Intentionally blank; automatically set in .gitlab-ci.yml

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (('GitLab', 'https://gitlab.com/muxync'),)

# Social widget
SOCIAL = (('GitLab', 'https://gitlab.com/muxync'),
          ('LinkedIn', 'https://www.linkedin.com/in/mark-mulligan-898b3962'))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Theme
# https://github.com/getpelican/pelican-themes/tree/master/pelican-bootstrap3/README.md
THEME = os.path.join((os.path.dirname(os.path.realpath(__file__))), 'themes', 'pelican-bootstrap3')
BOOTSTRAP_THEME = 'simplex'
PYGMENTS_STYLE = 'monokai'

# Extra
STATIC_PATHS = ['extra', 'images']
EXTRA_PATH_METADATA = {'extra/robots.txt': {'path': 'robots.txt'},
                       'extra/favicon.ico': {'path': 'favicon.ico'}}

# Ignore files
IGNORE_FILES = ['.#*', '__pycache__', 'README.md']

# GitLab pages requires 'public' for OUTPUT_PATH
OUTPUT_PATH = 'public'

# Plugins
PLUGIN_PATHS = [os.path.join((os.path.dirname(os.path.realpath(__file__))), 'plugins')]
PLUGINS = ['i18n_subsites', 'tag_cloud', 'tipue_search']
JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n']
}
DIRECT_TEMPLATES = ['index', 'tags', 'categories', 'authors', 'archives', 'search']

SITELOGO = 'images/logo.png'
SITELOGO_SIZE = 24
FAVICON = 'favicon.ico'
ABOUT_ME = "All good things"
BANNER = 'images/banner.png'
BANNER_SUBTITLE = 'This is my subtitle'
DISPLAY_TAGS_ON_SIDEBAR = True
DISPLAY_TAGS_INLINE = True
DISPLAY_CATEGORIES_ON_SIDEBAR = True

# CC_LICENSE doesn't support CC0 as a Creative Commons License type and this upstream pull request:
# https://github.com/getpelican/pelican-themes/pull/668
# hasn't been accepted/merged so I'll implement it via CUSTOM_LICENSE instead
# To use a supported license instead of CUSTOM_LICENSE set: CC_LICENSE = 'CC-BY'
CUSTOM_LICENSE = '<a rel="license" href="https://creativecommons.org/publicdomain/zero/1.0/"><img alt="Creative Commons License" style="border-width:0" src="//i.creativecommons.org/p/zero/1.0/80x15.png"></a> Content licensed under a <a rel="license" href="https://creativecommons.org/publicdomain/zero/1.0/">CC0 1.0 Universal (CC0 1.0) Public Domain Dedication</a>, except where indicated otherwise.'
