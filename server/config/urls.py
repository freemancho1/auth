from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt import views


urlpatterns = [
    path('admin/', admin.site.urls),
    
    # JWT token 발행(인증작업 시 수행)
    path('api/token/', views.token_obtain_pair),
    # JWT token 검증(데이터 요청 시? 수행)
    path('api/token/verify/', views.token_verify),
    # JWT REFRESH token 갱신(JWT token 소멸 시? 수행)
    path('api/token/refresh/', views.token_refresh),
    
    path('api/blog/', include('blog.urls')),
]
