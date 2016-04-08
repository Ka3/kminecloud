from django.contrib import admin

# Register your models here.
from .models import IRM_Ethinicity,IRM_Title,IRM_Location,Marital_Status,Report_Status,Case_Type,Panel_Role,Panel_Recommendations,Test_Person,Agency_Type,IRM_Agency
from .models  import IRM_Agency_Admin_Contact

@admin.register(IRM_Ethinicity,IRM_Title,IRM_Location,Marital_Status,Report_Status,Case_Type,Panel_Role,Panel_Recommendations,Agency_Type)
class Types_admin(admin.ModelAdmin):
    pass

admin.site.register(Test_Person)

admin.site.register(IRM_Agency)

admin.site.register(IRM_Agency_Admin_Contact)