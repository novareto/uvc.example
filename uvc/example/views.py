# -*- coding: utf-8 -*-
# # Copyright (c) 2007-2019 NovaReto GmbH
# # cklinger@novareto.de 

import grok

from zope.interface import Interface
from uvcsite.browser import Page


grok.templatedir('templates')


class LandingPage(Page):
    grok.context(Interface)
    grok.name('index')
