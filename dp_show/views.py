import json

from django.http import JsonResponse
from django.shortcuts import render
from dp_show.models import ImgInfo
from dp_user.models import UserInfo


def to_json(request, datas):
    data = {}
    data['list'] = list(datas)
    return json.dumps(data)


def index(request):
    user_id = request.session.get('user_id', '')
    alldraw = ImgInfo.objects.all().order_by('-itime')
    hotdraw = alldraw.order_by('-iclick')[0:15]
    newdraw = alldraw.order_by('-itime')[0:15]
    bestdraw = alldraw.order_by('-ipraise')[0:15]
    if user_id:
        user = UserInfo.objects.filter(pk=user_id)[0]
        mydraw = user.imginfo_set.all().order_by('-ipraise')
        context = {
            'login': 1,
            'user': user,
            'alldraw': alldraw,
            'hotdraw': hotdraw,
            'newdraw': newdraw,
            'bestdraw': bestdraw,
            'mydraw': mydraw,
        }
        return render(request, 'dp_show/index1.html', context)
    else:
        context = {
            # 'alldraw': alldraw,
            'hotdraw': hotdraw,
            'newdraw': newdraw,
            'bestdraw': bestdraw,
        }
        return render(request, 'dp_show/index1.html', context)


def center(request, uid):
    user = UserInfo.objects.filter(pk=uid)[0]
    mydraw = user.imginfo_set.all().order_by('-ipraise')
    context = {
        'user': user,
        'mydraw': mydraw,
        'error_name': '',
    }
    return render(request, 'dp_show/center.html', context)

#
# def test(request):
#     return render(request, 'dp_show/test.html')
#
#
# def test1(request):
#     page1 = request.GET['page1']
#     page2 = request.GET['page2']
#     list = ImgInfo.objects.filter(id__gt=page1).filter(id__lt=page2)
#     num = ImgInfo.objects.count()
#     list2 = []
#     for a in list:
#         list2.append({'id': a.pk, 'ititle': a.ititle, 'img': str(a.iimg)})
#     return JsonResponse({'count': num, 'data': list2})
