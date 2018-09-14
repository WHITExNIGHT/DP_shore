from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import *
from hashlib import sha1




def register(request):
    return render(request, 'dp_user/register.html', {'title': '注册'})


def register_handle(request):
    # 接收用户输入
    post = request.POST
    uname = post.get('user_name')
    upwd = post.get('pwd')
    upwd2 = post.get('cpwd')
    uemail = post.get('email')

    if len(uname) < 8:
        return redirect('/user/register/')
    count = UserInfo.objects.filter(uname=uname).count()
    if count > 0:
        # return render(request, '/user/register/', {'count': count})
        # return redirect('/user/register/')
        return render(request, 'dp_user/register.html', {'error': 1})
    if upwd == '':
        return redirect('/user/register/')
    if uemail == '':
        return redirect('/user/register/')
    # 判断密码
    if upwd != upwd2:
        return redirect('/user/register/')
    # 密码加密
    s1 = sha1()
    s1.update(upwd.encode("utf-8"))  # 指定编码格式，否则会报错
    upwd3 = s1.hexdigest()
    # 创建对象
    user = UserInfo()
    user.uname = uname
    user.upwd = upwd3
    user.uemail = uemail
    user.unickname = '新用户' + str(uemail)
    user.save()
    # 注册成功，转到登录页面
    return redirect('/user/login/')


def login(request):
    uname = request.COOKIES.get('uname', '')
    context = {'title': '登录', 'error_name': 0, 'error_pwd': 0, 'uname': uname}
    return render(request, 'dp_user/login.html', context)


def login_handle(request):
    # 接收请求信息
    post = request.POST
    uname = post.get('username')
    upwd = post.get('pwd')
    jizhu = post.get('jizhu', 0)
    # 根据用户登录查询对象
    users = UserInfo.objects.filter(uname=uname)  # []
    print(uname)
    # 判段用户名是否准确，准确则继续判断密码
    if len(users) == 1:
        s1 = sha1()
        s1.update(upwd.encode("utf-8"))
        if s1.hexdigest() == users[0].upwd:
            red = HttpResponseRedirect('/')
            # 记住用户名
            if jizhu != 0:
                red.set_cookie('uname', uname)
            else:
                red.set_cookie('uname', '', max_age=-1)
            request.session['user_id'] = users[0].id
            request.session['user_name'] = uname
            return red
        else:
            context = {'title': '用户登录', 'error_name': 0, 'error_pwd': 1, 'uname': uname, 'upwd': upwd}
            return render(request, 'dp_user/login.html', context)
    else:
        context = {'title': '用户登录', 'error_name': 1, 'error_pwd': 0, 'uname': uname, 'upwd': upwd}
        return render(request, 'dp_user/login.html', context)


def index(request):
    return render(request, 'dp_user/index.html')


def center_handle(request):
    user_id = request.session.get('user_id')
    user = UserInfo.objects.filter(pk=user_id)[0]

    # 接收用户输入
    post = request.POST
    unickname = post.get('unickname')
    upwd = post.get('upwd')
    uaddress = post.get('uaddress')
    uphone = post.get('uphone')

    if len(unickname) < 0:
        return render(request, 'dp_show/center.html', {'user': user, 'error_name': '请输入用户名！'})
    count = UserInfo.objects.filter(unickname=unickname).count()
    if count > 0 and user.unickname != unickname:
        return render(request, 'dp_show/center.html', {'user': user, 'error_name': '用户名已存在！'})
    if len(upwd) > 0:
        s1 = sha1()
        s1.update(upwd.encode("utf-8"))
        if s1.hexdigest() == user.upwd:
            unpwd = post.get('unpwd')
            uncpwd = post.get('uncpwd')
            if unpwd == uncpwd:
                s2 = sha1()
                s2.update(unpwd.encode("utf-8"))  # 指定编码格式，否则会报错
                npwd = s2.hexdigest()
                user.upwd = npwd
            else:
                return render(request, 'dp_show/center.html', {'user': user, 'error_npwd': '两次密码不一致！'})
        else:
            return render(request, 'dp_show/center.html', {'user': user, 'error_pwd': '密码错误！'})

    user.uaddress = uaddress
    user.uphone = uphone
    user.unickname = unickname
    user.save()
    # mydraw = user.imginfo_set.all().order_by('-ipraise')
    context = {
        'user': user,
        # 'mydraw': mydraw,
    }
    return render(request, 'dp_show/center.html', context)


def center_handle2(request):
    user_id = request.session.get('user_id')
    user = UserInfo.objects.filter(pk=user_id)[0]
    post = request.POST
    uintro = post.get('uintro')
    if len(uintro) > 200:
        context = {
            'user': user,
            'error_intro': '字数超过200！'
        }
        return render(request, 'dp_show/center.html', context)
    user.uintro = uintro
    user.save()
    context = {
        'user': user,
        # 'mydraw': mydraw,
    }
    return render(request, 'dp_show/center.html', context)


def logout(request):
    request.session.flush()
    return redirect('/user/login')
