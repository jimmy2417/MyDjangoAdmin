from myadmin.service import v1
from app01 import models
from django.utils.safestring import mark_safe

class MyAdminUserInfo(v1.BaseMyDjangoAdmin):

    def edit(self,row_obj):
        """
        生成编辑按钮，里面包含了我们反向生成的链接，并且包含了每一行数据对象的id
        :param row_obj: 获取到的每一行的数据对象
        :param self:  实例化出来的对象，里面包含了我们需要使用的所有的数据
        :return: 
        """
        from django.urls import reverse
        app_name = self.model_class._meta.app_label
        model_name = self.model_class._meta.model_name
        name = "%s:%s_%s_change" %(self.site.namespace,app_name,model_name)
        url = reverse(name,args=(row_obj.pk,))
        return mark_safe('<a href="%s">编辑</a>' %(url,))


    def checkbox(self,row_obj):
        """
        定制的checkbox控件
        :param row_obj: 
        :return: 
        """
        return mark_safe('<input type="checkbox" value="%s" />' % (row_obj.pk,))
    list_display = [checkbox,'id', 'username', 'email',edit]


v1.site.register(models.UserInfo,MyAdminUserInfo)


class MyAdminRole(v1.BaseMyDjangoAdmin):
    list_display = ['id','name']

v1.site.register(models.Role,MyAdminRole)


