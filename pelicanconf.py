#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

AUTHOR = 'Mark Mulligan'
SITENAME = 'MarkLog'
SITEURL = ''

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
LINKS = (('Contact', 'mailto:contact[AYAT]muxync[DAWT]net <Mark Mulligan>'),)

# Social widget
SOCIAL = (('GitLab', 'https://gitlab.com/muxync'),
          ('LinkedIn', 'https://www.linkedin.com/in/mark-mulligan-898b3962'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Theme
THEME = os.path.join((os.path.dirname(os.path.realpath(__file__))), 'theme')

# Extra
STATIC_PATHS = ['extra']
EXTRA_PATH_METADATA = {'extra/robots.txt': {'path': 'robots.txt'},
                       'extra/favicon.ico': {'path': 'favicon.ico'}}

# GitLab pages requires 'public' for OUTPUT_PATH
OUTPUT_PATH = 'public'
