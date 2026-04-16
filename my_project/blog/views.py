from django.views import generic
from .models import Post

class PostView(generic.ListView):
    queryset = Post.objects.filter(status='published').order_by('-created')
    template_name = 'index.html' 
    context_object_name = 'post_list'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post-detail.html'