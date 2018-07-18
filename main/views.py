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
        for thought in thoughts:
            if type(thought) != type(self.thought):
                thoughts.remove(thought)
        return thoughts
    
class ThoughtDetail(generic.DetailView):
    model = Thought
    template_name='thought_detail.html'