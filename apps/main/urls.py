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
    path('blog/marketplace-django-react/', views.BlogMarketplaceView.as_view(), name='blog_marketplace'),
    path('blog/integracion-stripe-openai/', views.BlogStripeOpenAIView.as_view(), name='blog_stripe_openai'),
    path('blog/cicd-gitlab-kubernetes/', views.BlogCICDView.as_view(), name='blog_cicd'),

]

api_urlpatterns = [
    path('api/services/<int:pk>/', api_views.ServiceDetailView.as_view(), name='service_detail'),
]


urlpatterns += api_urlpatterns
