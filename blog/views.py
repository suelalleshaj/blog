from django.views.generic import  ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post, Comment

class BlogView(ListView):
    model = Post
    template_name = 'firstpage.html'

class BlogListView(ListView):
    model = Post
    template_name = 'home.html'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'author', 'body']

    #def post(self, request, *args, **kwargs):


        #user = request.user
        #title = request.POST.get('title')

       # return super().post(request,args,kwargs)


class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']

class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')

class AddCommentView(CreateView):
    model = Comment
    fields = ['author','body']
    template_name = 'add_comment.html'
    success_url = reverse_lazy('home')

    def form_valid(self,form):
       form.instance.post_id = self.kwargs['pk']
       return super().form_valid(form)

class CommentDeleteView(DeleteView):
    model = Comment
    template_name = 'Comment_delete.html'
    success_url = reverse_lazy('home')

class CommentDetailView(DetailView):
    model = Comment
    template_name = 'comment_detail.html'



