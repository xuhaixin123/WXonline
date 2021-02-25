
from django.urls import path,include,re_path
from django.views.generic import TemplateView
from user.views import IndexView, LoginView, RegisterView, ActiveUserView, ForgetPwdView, ResetView, ModifyPwdView, LogoutView
from organization.views import OrgView
from django.views.static import serve
from WXonline.settings import MEDIA_ROOT
import xadmin
urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('index/', IndexView.as_view(), name='index'),
    # path('',  TemplateView.as_view(template_name='index.html'),name='index'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('captcha/', include('captcha.urls')),
    re_path('active/(?P<active_code>.*)/', ActiveUserView.as_view(), name='user_active'),
    path('forget/', ForgetPwdView.as_view(), name='forget_pwd'),
    re_path('reset/(?P<active_code>.*)/', ResetView.as_view(), name='reset_pwd'),
    path('modify_pwd/', ModifyPwdView.as_view(), name='modify_pwd'),
    # 处理图片显示的url,使用Django自带serve,传入参数告诉它去哪个路径找，我们有配置好的路径MEDIAROOT
    re_path(r'^media/(?P<path>.*)', serve, {"document_root": MEDIA_ROOT }),
    # 课程机构app相关url配置
    path("org/", include('organization.urls', namespace="org")),
    # 课程app相关url配置
    path("course/", include('course.urls', namespace="course")),
    # 个人信息
    path("user/", include('user.urls', namespace="user")),
]
