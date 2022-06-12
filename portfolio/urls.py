from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('apresentacao', views.apresentacao_page_view, name='apresentacao'),
    path('projetos', views.projetos_page_view, name='projetos'),
    path('spa', views.spa_page_view, name='spa'),

    path('pw', views.pw_page_view, name='pw'),
    path('blog', views.blog_page_view, name='blog'),
    path('novo', views.novo_post_page_view, name='novo'),
    path('quizz', views.quizz_page_view, name='quizz'),
    path('resultados', views.resultados_page_view, name='resultados'),


    path('novoProjeto/', views.novo_projetos_page_view, name='novoProjeto'),
    path('editar_projeto/<int:projeto_id>', views.view_editar_projeto, name='editarProjeto'),
    path('apagar_projeto/<int:projeto_id>', views.view_apagar_projeto, name='apagarProjeto'),

    path('novaCadeira/', views.nova_cadeira_page_view, name='novaCadeira'),
    path('editar_cadeira/<int:cadeira_id>', views.view_editar_cadeira, name='editarCadeira'),
    path('apagar_cadeira/<int:cadeira_id>', views.view_apagar_cadeira, name='apagarCadeira'),

    path('novoTFC/', views.novo_tfc_page_view, name='novoTFC'),
    path('editar_TFC/<int:tfc_id>', views.view_editar_tfc, name='editarTFC'),
    path('apagar_TFC/<int:tfc_id>', views.view_apagar_tfc, name='apagarTFC'),

    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
