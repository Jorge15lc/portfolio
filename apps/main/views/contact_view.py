from django.views.generic import TemplateView


class ContactView(TemplateView):
    template_name = 'main/contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['form'] = ContactForm()
        return context

    # def post(self, request, *args, **kwargs):
    #     form = ContactForm(request.POST)
    #     if form.is_valid():
    #         form.send_email()
    #         messages.success(request, 'Your message was sent successfully.')
    #         return redirect('main:contact')
    #     return render(request, self.template_name, {'form': form})