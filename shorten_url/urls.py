from django.urls import path
from shorten_url import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create_short_url/', views.CreateShortUrlView.as_view(), name='create_short_url'),
    path('short_url/<str:shortened_url>/', views.create_short_url, name='create_short_url_def'),
    path('<str:link>/', views.redirect_url, name='redirect_url'),
]
