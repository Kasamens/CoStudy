from django.views import generic
from .models import Post
from django.http import HttpResponse

class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'latest_post_list'

    def get_queryset(self):
        """Return the last 100 published posts"""
        return Post.objects.order_by('-pub_date')[:100]

class PostDetail(generic.DetailView):
    model = Post
    template_name='post_detail.html'
