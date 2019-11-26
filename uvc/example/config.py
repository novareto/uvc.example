# -*- coding: utf-8 -*-
# # Copyright (c) 2007-2019 NovaReto GmbH
# # cklinger@novareto.de 



import uvcsite

from uvcsite.content.productregistration import ProductRegistration
from uvcsite.tests.fixtures.addressbook import AddressBook



class AdrBookReg(ProductRegistration):
    key = "adrbook"
    title = u"Adressbuch"

    def available(self):
        return True

    def factory(self, *args, **kwargs):
        return AddressBook()


