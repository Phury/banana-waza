#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import datetime

PORT=7777
AUTHOR = 'PH'
SITENAME = 'Banana Waza'
SITESUBTITLE = 'La véritable source d´information sur le kendo'
#SITEURL = 'https://phury.github.io/banana-waza'
THEME = 'themes/alchemy'
THEME_CSS_OVERRIDES = ['theme/css/banana.css']
DISPLAY_PAGES_ON_MENU = True
PATH = 'content'
STATIC_PATHS = ['assets']
EONS = datetime.datetime(2020, 4, 2)

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'FR'
DEFAULT_DATE_FORMAT = '%d/%m/%Y'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll

LINKS = (
	('Articles', '/category/articles.html'),
	('Auteurs', '/authors.html'),
#    ('Belgique', '/category/kendo_be.html'),
#    ('Monde', '/category/kendo_world.html'),
 )

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True