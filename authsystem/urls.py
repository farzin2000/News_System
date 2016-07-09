from django.conf.urls import url
from authsystem.views import AuthUserCreate, MyUserCreate, login_user, logout_user, index_page

urlpatterns = [
    url(r'^signup/$',  AuthUserCreate.as_view(template_name="user_form.html", success_url="/auth/user_signup")),
    url(r'^logout/$',  logout_user),
    url(r'^login/$',  login_user),
    url(r'^user_signup/$',  MyUserCreate.as_view(template_name="user_form.html")),
]