from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.models import User
from .models import * 
from django.views.generic import (
    ListView,
	DetailView,
    CreateView,
    DeleteView,
    UpdateView,      
)
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, Http404
from .forms import *
from django .core.paginator import Paginator
from .filters import PostFilter
from django.db.models import Q
from django.template.loader import render_to_string



def home(request):
    posts= Post.published.all().order_by('-date_posted')
    paginator=Paginator(posts,5)
    page=request.GET.get('page')
    posts=paginator.get_page(page)
    
    query=request.GET.get('q')
    if query:
        posts = Post.published.filter(
        Q(title__icontains=query)|
        Q(author__username=query)|
        Q(content__icontains=query)
        )
    print(query)


    context = {
        'posts': posts,
    }
    
    return render(request, 'blog_app/home.html', context)


class NewPostView(LoginRequiredMixin,SuccessMessageMixin, CreateView):
    model = Post
    success_url = '/'
    #success_message = "Post successfully added"
    fields = ['title', 'content','image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form) 


class PostDelView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin,SuccessMessageMixin, UpdateView):
    model = Post
    success_url = '/'
    #success_message = "Article successfully Updated"
    fields = ['title', 'content','image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form) 
        
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False         

class UserPostView(ListView):
    model = Post
    template_name = 'blog_app/user_posts.html' 
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')           


def post_detail(request,pk):
    post= get_object_or_404(Post,pk=pk)
    comments = Comment.objects.filter(post=post, reply=None).order_by('-id')
    is_liked = False
    is_favourite = False
    if post.likes.filter(id=request.user.id).exists():
        is_liked = True

    if post.favourite.filter(id=request.user.id).exists():
        is_favourite = True    

    if request.method == 'POST':
        comment_form = CommentForm(request.POST or None)
        if comment_form.is_valid():
            body = request.POST.get('body')
            reply_id = request.POST.get('comment_id')
            comment_qs = None
            if reply_id:
                comment_qs = Comment.objects.get(id=reply_id)
            comment = Comment.objects.create(post=post, user=request.user, body=body, reply=comment_qs)
            comment.save()  
            return HttpResponseRedirect(post.get_absolute_url())

    else:
         comment_form= CommentForm()    

    context = {
        'post': post,
        'is_liked': is_liked,
        'is_favourite': is_favourite,
        'total_likes': post.total_likes(),
        'comments': comments,
        'comment_form': comment_form,
    }
    if request.is_ajax():
        html = render_to_string('blog_app/comments.html', context, request=request)
        return JsonResponse({'form': html})

    return render(request, 'blog_app/post_detail.html', context)     



def post_favourite_list(request):
    user = request.user
    favourite_posts = user.favourite.all()
    context = {
        'favourite_posts': favourite_posts,
    }
    return render(request, 'blog_app/post_favourite_list.html', context)



def favourite_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.favourite.filter(id=request.user.id).exists():
        post.favourite.remove(request.user)
    else:
        post.favourite.add(request.user)
    return HttpResponseRedirect(post.get_absolute_url())



def like_post(request):
    #post = get_object_or_404(Post, id=request.POST.get('post_id'))
    post = get_object_or_404(Post, id=request.POST.get('id'))
    is_liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        is_liked = False
    else:
        post.likes.add(request.user)
        is_liked = True
    
    context = {
        'post': post,
        'is_liked': is_liked,
        'total_likes': post.total_likes(),
        
    }
    #return HttpResponseRedirect(post.get_absolute_url())
    if request.is_ajax():
        html = render_to_string('blog_app/like_section.html', context, request=request)
        return JsonResponse({'form': html})
    
def video(request):
    obj= Video.objects.all()
    context= {'obj': obj}
        
      
    return render(request, 'blog_app/videos.html', context)   



def file(request):
    context= {'file': FileAdmin.objects.all()} 
    return render(request, 'blog_app/file.html', context)  

def download(request,path):
    file_path=os.path.join(settings.MEDIA_ROOT,path)
    if os.path.exists(file_path):
        with open(file_path,'rb')as fh:
            response=HttpResponse(fh.read(),content_type="application/fileupload")
            response['Content-Disposition']='inline;filename='+os.path.basename(file_path)
            return response      
    raise Http404      