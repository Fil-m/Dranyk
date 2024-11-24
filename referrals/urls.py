from django.urls import path
from . import views  # Переконайтеся, що імпорт правильний

urlpatterns = [
    path('create/', views.create_referral_link, name='create_referral_link'),
    path('r/<str:referral_code>/', views.redirect_referral_link, name='redirect_referral_link'),
    path('list/', views.referral_link_list, name='referral_link_list'), 
]
