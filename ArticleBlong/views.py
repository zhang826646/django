#v1.0
#  from django.http import HttpResponse
#
# def index(request):
#     return  HttpResponse("<h2 style='color:red;'>hello</h2>")
#
# def introduce(request,name,age):
#     return  HttpResponse("i am {},i am {} yeas old".format(name,age))

# v2.0
from django.http import HttpResponse      #返回http响应
from django.template.loader import get_template     #用来记载settings的TEMPLATES配置中的回弹模量页面

def index(request):
    template=get_template("index.html")    #加载页面
    result=template.render({'name':'laoli'})   #类似字符串的渲染
    return HttpResponse(result)  #返回的内容是需要渲染的结果

def bage_list(request,bage):
    bage=int(bage)
    template=get_template("bage_list.html")
    result=template.render({"bage":bage})
    return HttpResponse(result)