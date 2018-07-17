from django.views import generic
from .models import Thought


class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'latest_thought_list'
    thought = None

    def __init__(self, thought):
        self.thought = thought

    def get_queryset(self):
        thoughts = list(Thought.objects.all())
        thoughts.remove(thought) if thought.get_serial() != self.thought.get_serial()
        return thoughts

class ThoughtDetail(generic.DetailView):
    model = Thought
    template_name='thought_detail.html'