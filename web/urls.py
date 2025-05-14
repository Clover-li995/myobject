#前台大堂点餐端子路由配置文件
from django.urls import path,include
from web.views import index

urlpatterns = [
    path('', index.index, name='index'),

    #前台登陆退出的路由
    path('login', index.login, name='web_login'),  # 加载登陆表单
    path('dologin', index.dologin, name='web_dologin'),  # 执行登陆表单
    path('logout', index.logout, name='web_logout'),  # 退出
    path('verify', index.verify, name='web_verify'),  # 输出验证码

    #为url路由添加请求前缀web/,凡是带此前缀的url地址必须登陆后才可访问
    path('web/',include([
    path('', index.webindex, name='web_index'), #前台大堂点餐首页
    ]))


]