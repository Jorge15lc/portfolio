from typing import Any
from django.views.generic import ListView
from apps.main.models import Work, Category

class ProjectsView(ListView):
    template_name = 'projects/projects.html'
    model = Work
    paginate_by = 50
    context_object_name = 'works'
    ordering = ['-created']

    def get_context_data(self, **kwargs):
        context  = super().get_context_data(**kwargs)
        
        context['categories'] = Category.objects.filter(works__isnull=False).distinct()

        return context 