from django.views.generic import TemplateView
from ..models import Work, Category


class HomeView(TemplateView):
    template_name = 'home/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['works'] = Work.objects.all()
        context['categories'] = Category.objects.filter(works__isnull=False).distinct()

        return context