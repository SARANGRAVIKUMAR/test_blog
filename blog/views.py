from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, View
from .models import Blog
from .forms import BlogForm, CommentForm


class BlogView(ListView):
    model = Blog
    template_name = 'blog.html'
    paginate_by = 6
    ordering = ['-date_created']
    context_object_name = 'posts'



# class BlogDetailView(DetailView):
#     model = Blog
#     template_name = "blog_details.html"
#     context_object_name = 'post'


def BlogDetailView(request, pk):
    post = Blog.objects.get(pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog = post
            comment.save()
            return redirect('blog')

    form = CommentForm()
    context = {
        'post': post,
        'form': form,
    }
    return render(request, "blog_details.html", context)


def forms(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            print("valid")
            form.save()
            return redirect('blog')

    form = BlogForm()
    return render(request, 'form.html', {'form': form})
