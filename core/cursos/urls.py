from django.urls import path
from .views import *
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('cursos', CursoViewSet)
router.register('avaliacoes', AvaliacaoViewSet)

urlpatterns = [
    path('cursos/', CursosAPIView.as_view(), name='curso-list'),
    path('cursos/<int:pk>/', CursoAPIView.as_view(), name='curso-detail'),

    path('avaliacoes/', AvaliacoesAPIView.as_view(), name='avaliacao-list'),
    path('avaliacoes/<int:avaliacao_pk>/', AvaliacaoAPIView.as_view(), name='avaliacao-detail'),

    path('cursos/<int:curso_pk>/avaliacoes/', AvaliacoesAPIView.as_view(), name='curso-avaliacoes'),
    path('cursos/<int:curso_pk>/avaliacoes/<int:avaliacao_pk>/', AvaliacaoAPIView.as_view(), name='curso-avaliacao-detail'),
]

__all__ = ["urlpatterns", "router"]
