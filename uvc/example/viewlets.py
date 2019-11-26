import grok
import uvcsite.browser.layout.slots


from uvc.menus.components import MenuItem

from uvc.menus.directives import menu
from uvc.siguvtheme.skin import ISiguvTheme
from zope import interface


class LogOutMenuEntry(MenuItem):
    grok.layer(ISiguvTheme)
    menu(uvcsite.browser.layout.slots.interfaces.IQuickLinks)
    grok.order(20)

    title = "Logout"
    icon = "fas fa-sign-out-alt"

    def url(self):
        return self.view.application_url() + "/logout"
