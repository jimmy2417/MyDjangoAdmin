from django.template import Library
from types import FunctionType


register = Library()

def data_body(result_list,list_display,my_admin_obj):
    """
    取到数据库中的数据及定制化显示的字段列表传递给模板中，前端模板以表格的形式显示出来
    :param result_list: 
    :param list_display: 
    :return: 
    """

    for row in result_list:
        yield [ name(my_admin_obj,row) if isinstance(name,FunctionType) else getattr(row,name) for name in list_display]

def data_head(list_display,my_admin_obj):
    """
    取到定制的标题
    :return: 
    """
    yield list_display


@register.inclusion_tag('yg/md.html')
def func(result_list,list_display,my_admin_obj):
    v = data_body(result_list,list_display,my_admin_obj)
    t = []
    for item in list_display:
        # print(item,ygadmin_obj.model_class)
        if isinstance(item,FunctionType):
            t.append(item.__name__.title())
        else:
            t.append(item)
    print(t)
    return {'xxxx':v,'tttt':t}