from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from Tarefas.urls import Trouter
from Usuario.urls import Urouter

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('admin', admin.site.urls),
    path('login', views.obtain_auth_token),
    path('', include(Urouter.urls)),
    path('', include(Trouter.urls)),
]