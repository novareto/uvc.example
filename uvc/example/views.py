# -*- coding: utf-8 -*-
# # Copyright (c) 2007-2017 NovaReto GmbH
# # cklinger@novareto.de


import grok
import uvcsite

from time import sleep
from zope import interface

#from uvc.tbskin.resources import TBSkinViewlet


#class TBSkinViewlet(TBSkinViewlet):
#    pass


class Index(uvcsite.browser.Page):
    grok.context(interface.Interface)

    def render(self):
        return u" HALLO WELT"
