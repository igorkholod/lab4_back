from django.urls import path
from . import views
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

urlpatterns = [
    path('drug/<int:id>/', views.DrugView.as_view()),
    path('pharmacy/<int:id>/', views.PharmacyView.as_view()),
    path('search/<str:search>/', views.DrugSearchView.as_view()),
    path('search_pharmacy/<int:id>/', views.PharmacySearchView.as_view()),
    path('auth/obtain_token/', obtain_jwt_token),
    path('auth/refresh_token/', refresh_jwt_token),
    path('auth/register/', views.RegisterView.as_view())
]
