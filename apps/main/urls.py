from django.urls import path
from apps.main import views
from apps.main.api import views as api_views

app_name = 'main'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('services/', views.ServicesView.as_view(), name='services'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('projects/', views.ProjectsView.as_view(), name='projects'),

]

api_urlpatterns = [
    path('api/services/<int:pk>/', api_views.ServiceDetailView.as_view(), name='service_detail'),
]


urlpatterns += api_urlpatterns
