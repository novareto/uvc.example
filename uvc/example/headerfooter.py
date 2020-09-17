# -*- coding: utf-8 -*-
# # Copyright (c) 2007-2019 NovaReto GmbH
# # cklinger@novareto.de


import grok


grok.templatedir('templates')


# Zunächst brauchen wir einen eigenen Layer. Dieser erbt von Default


from uvc.siguvtheme.skin import ISiguvTheme


class IExampleTheme(ISiguvTheme):
    grok.skin('exampletheme')


from uvc.siguvtheme.viewlets import Footer, GlobalMenu


class Footer(Footer):
    grok.layer(IExampleTheme)


class GlobalMenu(GlobalMenu):
    grok.layer(IExampleTheme)
