from django.views import generic
from django.urls import reverse,reverse_lazy
from .models import Post

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    

class PostCreate(generic.CreateView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:all")
    
class PostDetail(generic.DetailView):
    model = Post
    
class PostUpdate(generic.UpdateView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:all")
    
class PostDelete(generic.DeleteView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:all")
    


