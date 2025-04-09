from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

# ✅ Import the JWT views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

def home(request):
    return HttpResponse("Welcome to the academic Issue Tracking System (AITS)!")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),

    # ✅ Add JWT auth endpoints
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('', home),
]
