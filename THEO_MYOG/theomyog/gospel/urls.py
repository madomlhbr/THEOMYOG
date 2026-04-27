from django.urls import path
from . import views

urlpatterns = [
    # Change 'iron_rails_gospel' to 'landing_page'
    path('', views.landing_page, name='landing_page'),
    
    # Add the dynamic path for the stations
    path('station/<int:station_id>/', views.station_detail, name='station_detail'),
]