from django.urls import path,include
from . import views

urlpatterns = [
    path('api', include('api.urls')),
    path('stream', views.stream, name='stream'),
    path('data',views.generate_table,name='check'),
    path('pdcreate', views.generate_list, name='generagte_list'),
    path('reset_session', views.reset_session, name='reset'),
    path('', views.index, name='index'),
]