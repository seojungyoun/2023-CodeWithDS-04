from django.contrib import admin
from gradpage.models import Department, Display_info, Major, Archive


admin.site.register(Department)
admin.site.register(Major)
admin.site.register(Archive)
admin.site.register(Display_info)