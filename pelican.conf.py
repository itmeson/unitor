#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u"Mark Betnel"
SITENAME = u"Unitor"
SITEURL = 'http://markbetnel.com/unitor'

TIMEZONE = 'America/Los_Angeles'
GOOGLE_ANALYTICS = "UA-20141547-1"
DEFAULT_LANG='en'

DISQUS_SITENAME = 'unitor'

# Blogroll
LINKS =  (
     ('DESMOS', 'http://www.desmos.com'),
     ('Powers', 'http://www.powersof10.com/'),
     ('WolframAlpha', 'http://wolframalpha.com'),
     ('Google Calc', 'http://www.google.com/search?q=calculator')	
     )


DEFAULT_PAGINATION = 5 
DISPLAY_PAGES_ON_MENU = False

TAG_SAVE_AS = 'tag/{slug}.html'
TAG_URL = 'tag/{slug}.html'    

PLUGIN_PATH = '../../../pelican-plugins' 
PLUGINS = ['sitemap', 'create_calendar', 'ical', 'gallery', 'pelican-vimeo', 'pelican-youtube']


CC_LICENSE = "CC-BY"
