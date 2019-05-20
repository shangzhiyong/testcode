from django.shortcuts import render
import datetime
# Create your views here.
#视图文件
from  django.http import HttpResponse
from django.http import Http404
def index(request):
    return HttpResponse(u"我的第一段Django代码,哈哈哈，还挺好玩的")
def GetTime(request):
    now = datetime.datetime.now()
    return  HttpResponse(now)
def houes_ahead(request,offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now()+datetime.timedelta(hours=offset)
    html = "<html><body>In %s hours, it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)