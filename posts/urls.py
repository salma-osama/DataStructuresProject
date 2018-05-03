from django.conf.urls import url
from .import views
from accounts import views as accounts_views

app_name='posts'

urlpatterns = [
    url(r'^$',views.timeline,name="timeline"),
    url(r'^create/$',views.post_create, name="create"),
    url(r'^profile/$', accounts_views.view_my_profile,name="my_profile"),
    # url(r'^(?P<slug>[\w-]+)/$',accounts_views.view_profile,name="profile"),
    # url(r'^like/$',views.post_like, name="like"),
]
