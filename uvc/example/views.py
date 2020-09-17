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


from zope import schema, interface

class IPerson(interface.Interface):

    name = schema.TextLine(title=u"TEST")


from zeam.form.base import Fields, action
from uvcsite.browser import Form
class TForm(Form):
    grok.context(Interface)

    fields = Fields(IPerson)
    
    @action(u'Speichern')
    def handle_save(self):
        import pdb; pdb.set_trace()
        data, errors = self.extractData()
        print(errors)
