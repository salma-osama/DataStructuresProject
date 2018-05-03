from django.contrib import admin
from django.conf.urls import url,include
from .import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from accounts import views as accounts_views

app_name="base"

urlpatterns = [
    url('admin/', admin.site.urls), #admin.site.urls de haga build-in ll backend mn 3ndo
    url(r'^posts/',include('posts.urls')),
    url(r'^accounts/',include('accounts.urls')),
    url(r'^about/$',views.about), #here detecting if the user goes to this url and firing this particular function for him
    url(r'^$',views.homepage,name="home"),
    url(r'^profile/$',accounts_views.view_my_profile,name="my_profile"),

]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
