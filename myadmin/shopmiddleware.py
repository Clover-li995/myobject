#自定义中间类（执行是否登陆判断）
from django.shortcuts import redirect
from django.urls import reverse
import re

class ShopMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print('ShopMiddleware')

    def __call__(self, request):
        # 获取当前请求路径
        path = request.path
        print('url:',path)

        #判断管理后台是否登陆
        #定义后台不登陆也可以访问的url列表
        urllist = ['/myadmin/login','/myadmin/logout','/myadmin/dologin','/myadmin/verify']
        #判断当前请求url地址是否是以/myadmin开头，并且不在 urllist 中，才做是否登陆判断
        if re.match(r'^/myadmin',path) and (path not in urllist):
            # 判断是否登陆(在session中没有adminuser)
            if 'adminuser' not in request.session:
                # 重定向到登陆页
                return redirect(reverse('myadmin_login'))
                #pass

       #判断大堂点餐请求的判断，判断是否登陆（session中是否有webuser）
        if re.match(r'^/web',path):
            # 判断是否登陆(在session中没有webuser)
            if ('webuser') not in request.session:
                # 重定向到登陆页
                return redirect(reverse('web_login'))
                #pass


        response = self.get_response(request)
        return response