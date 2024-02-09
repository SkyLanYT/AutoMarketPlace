from django.urls import path, re_path
from . import views
from django.conf.urls.static import static
from django.conf import settings

from .views import RegistrationUser, AuthUser, home, logout_user, detail_user, add_advertisement


urlpatterns = [
    path('log_in/', AuthUser.as_view(), name='log_in'),
    path('reg/', RegistrationUser.as_view(), name='reg'),
    path('logout/', logout_user, name='logout'),
    path('account/', detail_user, name='detail_user'),
    re_path(r'^advertisement/$', views.add_advertisement, name='advertisement'),
    path('', views.index, name='home'),
    path('add_advertisement/', views.add_advertisement, name='add_advertisement'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
