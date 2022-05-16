from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('home', views.home_page_view, name='home'),
    path('apresentacao', views.apresentacao_page_view, name='apresentacao'),
    path('projetos', views.projetos_page_view, name='projetos'),
    path('pw', views.pw_page_view, name='pw'),
    path('blog', views.blog_page_view, name='blog'),
    path('site', views.site_page_view, name='site'),
]
