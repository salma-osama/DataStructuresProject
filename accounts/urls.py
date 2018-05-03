from django.conf.urls import url
from .import views
from posts import views as posts_views

app_name="accounts"

urlpatterns=[
url(r'^$',posts_views.timeline, name="timeline"),
url(r'^signup/$',views.signup_view,name="signup"),
url(r'^login/$',views.login_view, name="login"),
url(r'^logout/$',views.logout_view, name="logout"),
url(r'^my_profile/$', views.view_my_profile, name='my_profile'),
url(r'^my_profile/edit/$', views.edit_my_profile, name='edit_my_profile'),
url(r'^my_profile/password/$', views.edit_my_password, name='edit_my_password'),
url(r'^change-password/$', views.edit_my_password, name='edit_my_password'),
url(r'^my_profile/about_me/$',views.view_me, name="about_me"),
url(r'^profile/(?P<pk>\d+)/$', views.view_profile, name='profile_with_pk'), 
url(r'^(?P<friend>[\w-]+)/$',views.view_profile, name='profile'),
url(r'^profile/$', views.view_profile, name='profile'),
]
