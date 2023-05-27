from django.contrib import admin
from django.urls import path,include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', views.about,name = "about"),
    path('',views.home),
    path('articles/',include('articles.urls')),
    path('accounts/',include('accounts.urls')),

]

# urlpatterns += staticfiles_urlpatterns()
# urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

urlpatterns +=  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

    # ... the rest of your URLconf goes here ...
 # static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#
urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # ... the rest of your URLconf goes here ...
