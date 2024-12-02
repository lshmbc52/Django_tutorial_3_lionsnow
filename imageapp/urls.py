from django.urls import path
from . import views

app_name='imageapp'

urlpatterns = [   
    # 카테고리 관리
    path('', views.index, name='index'), 
]