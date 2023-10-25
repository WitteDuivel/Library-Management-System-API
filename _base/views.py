from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class _baseIndexView(TemplateView):
    pass


class _baseCreateView(CreateView):
    pass


class _baseUpdateView(UpdateView):
    pass


class _baseDeleteView(DeleteView):
    pass
