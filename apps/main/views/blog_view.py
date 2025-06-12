from django.views.generic import TemplateView

class BlogMarketplaceView(TemplateView):
    template_name = 'blog/marketplace_django_react.html'

class BlogStripeOpenAIView(TemplateView):
    template_name = 'blog/stripe_openai.html'

class BlogCICDView(TemplateView):
    template_name = 'blog/cicd_gitlab_kubernetes.html'
