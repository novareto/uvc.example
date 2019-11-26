# -*- coding: utf-8 -*-
#

import grok
import uvcsite
import logging

from uvc.example import log
from uvc.configpanel import get_plugin_configuration
from uvc.configpanel import Plugin
from uvcsite.auth.interfaces import ICOUser
from dolmen.security.policies import ExtraRoleMap
from zope.securitypolicy.interfaces import Allow, Deny
from zope.securitypolicy.securitymap import SecurityMap

from zope import schema, interface
from zope.interface import directlyProvides
from uvc.configpanel import Configuration
from uvc.configpanel import IConfigurablePlugin

from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from zope.schema.interfaces import IContextSourceBinder
from grokcore.component import provider
from zope.cachedescriptors.property import CachedProperty
from zeam.form.base import Fields


class ISecuritySettings(interface.Interface):
    """Mitbenutzeransicht"""

    canView = schema.Choice(
        title=u"Ansicht für Mitbenutzer",
        description=u"Sollen Ihre Mitbenutzer alle Dokumente \
                      oder nur Ihre selbst erstellten sehen können?",
        values=("alle", "eigene"),
        default="eigene",
    )


class HomeFolderDisplayCoUserPlugin(Plugin):
    grok.name("securitysettings")

    title = u"Ansichten Benutzerordner"
    description = u"Ansichten Benutzerordner"

    def getInterfaces(self):
        return [ISecuritySettings]

    @CachedProperty
    def configuration_fields(self):
        ifaces = self.getInterfaces()
        fields = Fields(*ifaces)
        fields["canView"].mode = "radio"
        return fields


class CoUserRole(grok.Role):
    grok.name("uvc.CoUser")
    grok.permissions("uvc.ViewContent")


# from uvc.unfallanzeige.interfaces import IUnfallanzeige
class SpecialSecurity(ExtraRoleMap, grok.Adapter):
    grok.context(uvcsite.content.interfaces.IContent)

    def _compute_extra_data(self):
        extra_map = SecurityMap()
        user = uvcsite.utils.shorties.getPrincipal()
        conf = get_plugin_configuration(name="securitysettings")
        log("Setting canView: %s" % conf.get("canView", False), severity=logging.DEBUG)
        if user.id.count("-") == 2:
            if conf.get("canView", "eigene") == "eigene":
                if user.id == self.context.principal.id:
                    extra_map.addCell("uvc.CoUser", user.id, Allow)
                    log(
                        "SETTING CO USER FOR %s %s" % (self.context.__name__, user.id),
                        severity=logging.DEBUG,
                    )
                else:
                    log(
                        "DENY CO USER FOR %s in %s " % (user.id, self.context.__name__),
                        severity=logging.DEBUG,
                    )
                    extra_map.addCell("uvc.Editor", user.id, Deny)
        return extra_map


# Sortierungsoptionen
#


@provider(IContextSourceBinder)
def getSortOn(context):
    return SimpleVocabulary(
        (
            SimpleTerm("table-link-1", "table-link-1", u"Titel"),
            SimpleTerm("table-state-3", "table-state-3", u"Workflow Status"),
            SimpleTerm("table-creator-4", "table-creator-4", u"Autor"),
            SimpleTerm("table-modified-5", "table-modified-5", u"Datum"),
        )
    )


@provider(IContextSourceBinder)
def getSortOrder(context):
    return SimpleVocabulary(
        (
            SimpleTerm("ascending", "ascending", u"Aufsteigend"),
            SimpleTerm("reverse", "reverse", u"Absteigend"),
        )
    )


class IFolderSorting(interface.Interface):

    sortOn = schema.Choice(
        title=u"Sortierkriterium",
        description=u"Nach welchen Kriterium wollen Sie Ihren Ordner sortieren?",
        source=getSortOn,
    )

    sortOrder = schema.Choice(title=u"Reihenfolge", source=getSortOrder)


class HomeFolderSortingPlugin(Plugin):
    grok.name("homefolder_sorting")
    grok.provides(IConfigurablePlugin)

    title = description = "Sortierung Benutzerordner"

    def getInterfaces(self):
        return [IFolderSorting]


from uvcsite.homefolder.views import Index
from uvc.siguvtheme.skin import ISiguvTheme


class Index(Index):
    grok.layer(ISiguvTheme)

    def getSortOrder(self):
        return get_plugin_configuration(name="homefolder_sorting").get(
            "sortOrder", u"ascending"
        )

    def getSortOn(self):
        return get_plugin_configuration(name="homefolder_sorting").get(
            "sortOn", "table-modified-5"
        )
