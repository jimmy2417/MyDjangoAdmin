from myadmin.service import v1
from app02 import models

class MyAdminUserGroup(v1.BaseMyDjangoAdmin):
    list_display = ['id','title']

v1.site.register(models.UserGroup,MyAdminUserGroup)
