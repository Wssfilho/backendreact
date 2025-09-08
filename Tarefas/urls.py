from .views import TarefaModelViewSet
from rest_framework.routers import DefaultRouter

Trouter = DefaultRouter()
Trouter.register(r'tarefa', TarefaModelViewSet, basename='Tarefa')

urlpatterns = Trouter.urls