
from django.shortcuts import render,HttpResponse
# from django.db import models
from types import FunctionType

from django.contrib import admin


class BaseMyDjangoAdmin(object):
    def __init__(self,model_class,site):
        self.model_class = model_class
        self.site = site

    @property
    def urls(self):
        from django.conf.urls import url,include
        info = self.model_class._meta.app_label,self.model_class._meta.model_name
        urlpatterns = [
            url(r'^$',self.changelist_view,name='%s_%s_changelist' % info),
            url(r'^add/$',self.add_view,name='%s_%s_add' % info),
            url(r'^(.+)/delete/$',self.delete_view,name='%s_%s_delete' % info),
            url(r'^(.+)/change/$',self.change_view,name='%s_%s_change' % info),

        ]
        return urlpatterns

    def changelist_view(self,request):
        """
        显示全部内容
        :return: 
        """
        result_list = self.model_class.objects.all()
        content = {
            'result_list':result_list,
            'list_display':self.list_display,
            'my_admin_obj':self,
        }
        return render(request,'yg/change_list.html',content)

    def add_view(self,request):
        """
        添加数据
        :return: 
        """
        info = self.model_class._meta.app_label, self.model_class._meta.model_name
        data = "%s_%s_add" % info
        return HttpResponse(data)

    def delete_view(self,request,pk):
        """
        删除数据
        :return: 
        """
        info = self.model_class._meta.app_label,self.model_class._meta.model_name
        data = "%s_%s_delete" % info
        return HttpResponse(data)

    def change_view(self,request,pk):
        """
        修改数据
        :param request: 
        :param pk: 
        :return: 
        """
        info = self.model_class._meta.app_label, self.model_class._meta.model_name
        data = "%s_%s_change" % info
        return HttpResponse(data)


class MyDjangoAdminSite(object):
    def __init__(self):
        self._registry = {}
        self.namespace = 'mydjangoadmin'
        self.app_name = 'mydjangoadmin'

    def register(self,model_class,temp_class = BaseMyDjangoAdmin):
        self._registry[model_class] = temp_class(model_class,self)

    def get_urls(self):
        from django.conf.urls import url,include
        ret = []
        for model_cls,myadmin_obj in self._registry.items():
            app_label = model_cls._meta.app_label
            model_name = model_cls._meta.model_name
            print(app_label,model_name)
            ret.append(url(r'%s/%s/'%(app_label,model_name),include(myadmin_obj.urls)))
        return ret

    @property
    def urls(self):
        return self.get_urls(),self.app_name,self.namespace

    def login(self,request):
        return HttpResponse('login')

    def logout(self,request):
        return HttpResponse('logout')

site = MyDjangoAdminSite()