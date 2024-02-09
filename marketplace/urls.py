from django.urls import path, include
from .views import index
from .views import log_in
from .views import reg

urlpatterns = [
    path('', index, name='index'),
    path('users/', include('users.urls')),
    # path('', include('django.contrib.aut.urls')),
]