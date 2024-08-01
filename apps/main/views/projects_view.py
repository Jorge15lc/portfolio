from django.views.generic import TemplateView

class ProjectsView(TemplateView):
    template_name = 'main/projects.html'
    