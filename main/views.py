from django.views import generic
from .models import Thought


class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'latest_thought_list'
    thought = None

    def __init__(self, thought):
        thought = thought

    def get_queryset(self):
        """Return the last 100 published thoughts"""
        return  Thought.objects.filter(type=thought.type)[:100]

""""
class ThoughtDetail(generic.DetailView):
    model = Thought
    template_name='thought_detail.html'
"""