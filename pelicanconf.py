#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

AUTHOR = u'Ethan House'
SITENAME = u'blog.ehouse.io'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'

DEFAULT_DATE_FORMAT = ('%B %d, %Y')

DESCRIPTION = "Tech and D&amp;D, what more could you want?"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

THEME = os.getcwd() + "/theme/"

PLUGIN_PATHS = [os.getcwd() +'/active-plugins']

PLUGINS = ['sitemap', 'gzip_cache']

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

MENUITEMS = (('Blog','/'),
      ('Projects','/projects.html'),
      ('D&amp;D','/dd.html'),
      ('About','/about.html'),)

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('Github', 'https://github.com/ehouse'),
      ('Keybase', 'https://keybase.io/ehouse'),
      ('Twitter','https://twitter.com/ewhhouse'),)

TWITTER_USERNAME = "ewhouse"

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

ARTICLE_URL = 'posts/{slug}.html'
ARTICLE_SAVE_AS = 'posts/{slug}.html'
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'

TAGS_SAVE_AS = ''
TAG_SAVE_AS = ''
