from menu import Menu, MenuItem
from django.core.urlresolvers import reverse


Menu.add_item("Agency", MenuItem("List Agencies",
                               reverse("IRM.views.list_agencies")))


Menu.add_item("Agency", MenuItem("Add Agency",
                               reverse("IRM.views.add_agency")))

Menu.add_item("Agency", MenuItem("Add Agency Admin",
                               reverse("IRM.views.add_agency_admin")))

Menu.add_item("Agency", MenuItem("List Agency Admins",
                               reverse("IRM.views.list_agency_admins")))


Menu.add_item("Panel_Members", MenuItem("List Members",
                               reverse("IRM.views.list_panel_members")))

Menu.add_item("Panel_Members", MenuItem("Add Panel Members",
                               reverse("IRM.views.add_panel_member")))


