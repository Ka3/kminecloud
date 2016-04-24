from django.contrib import admin
from reversion.admin import VersionAdmin

# Register your models here.
from .models import IRM_Ethinicity,IRM_Title,IRM_Location,Marital_Status,Report_Status,Panel_Role,Panel_Recommendations,Test_Person,Agency_Type,IRM_Agency,IRM_PanelContactRole,IRM_PanelContact
from .models import Case_Type,Agency_Decision

from .models  import IRM_Agency_Admin_Contact

class IRM_Agency_admin(VersionAdmin):
    pass

@admin.register(IRM_Ethinicity,IRM_Title,IRM_Location,Marital_Status,Panel_Role,Agency_Type)
class Types_admin(admin.ModelAdmin):
    pass

admin.site.register(Test_Person)

admin.site.register(IRM_Agency,IRM_Agency_admin)

admin.site.register(IRM_Agency_Admin_Contact)

admin.site.register(IRM_PanelContactRole)

admin.site.register(IRM_PanelContact)

admin.site.register(Agency_Decision)

admin.site.register(Panel_Recommendations)

admin.site.register(Case_Type)

admin.site.register(Report_Status)

