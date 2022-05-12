from django.shortcuts import render, redirect
from django.template.defaultfilters import slugify
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DeleteView, ListView

from .models import Blog, Tag, Category, Comment
from .forms import BlogForm, CommentForm, BlogUpdateForm
from accounts.models import CustomUser
from django.db.models import Q


class BaseView:
    def tag(self):
        tags = Tag.objects.all()
        return tags

    def category(self):
        categories = Category.objects.all()
        return categories


class BlogHome(View, BaseView):
    def get(self, request):

        categories = self.category()
        tags = self.tag()
        search = request.GET.get('search')
        if search:
            blog = Blog.objects.filter(
                Q(title__icontains=search) | Q(category__name__icontains=search)
            )
        else:
            blog = Blog.objects.all().order_by('-created')
        context = {
            'blogs': blog,
            'categories': categories,
            'tags': tags
        }

        return render(request, 'blog/home.html', context)


class CategoryBlog(View, BaseView):
    def get(self, request, slug):
        category = Category.objects.get(slug=slug)
        blog = Blog.objects.filter(category=category)

        context = {
            'category': category,
            'blogs': blog,
            'tags': self.tag(),
            'categories': self.category()
        }

        return render(request, 'blog/category.html', context)


class TagBlog(View, BaseView):
    def get(self, request, slug):
        tag = Tag.objects.get(slug=slug)
        blog = Blog.objects.filter(tags=tag)

        context = {
            'tag': tag,
            'blogs': blog,
            'categories': self.category(),
            'tags': self.tag()
        }

        return render(request, 'blog/tag_blog.html', context)


class BlogDetail(View, BaseView):
    def get(self, request, slug):
        blog = Blog.objects.get(slug=slug)
        form = CommentForm()

        context = {
            'blog': blog,
            'tags': self.tag(),
            'categories': self.category(),
            'form':form
        }

        blog.views += 1
        blog.save()
        return render(request, 'blog/blog_detail.html', context)

    def post(self, request, slug):
        form = CommentForm(request.POST)
        if form.is_valid():
            form_comment = form.save(commit=False)
            form_comment.blog = Blog.objects.get(slug=slug)
            form_comment.user = request.user
            form_comment.save()
            return redirect('blog_detail', form_comment.blog.slug)


class BlogCreate(View, BaseView):
    def get(self, request):
        form = BlogForm()

        context = {
            'form': form,
            'tags': self.tag(),
            'categories': self.category()
        }
        return render(request, 'blog/blog_create.html', context)

    def post(self, request):
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form_create = form.save(commit=False)
            form_create.slug = slugify(form_create.title)
            form_create.user = request.user
            form_create.save()
            form.save_m2m()
            return redirect('home')

# blogni o'chirish uchun class
class BlogDelete(DeleteView):
    model = Blog
    template_name = 'blog/blog_delete.html'
    success_url = reverse_lazy('home')

#categoriyalar uchun class
class CategoryBLogList(ListView):
    model = Category
    template_name = 'blog/categories.html'
    context_object_name = 'categories'

# komentariyani o'chirish uchun class
class CommentDelete(View):
    def post(self, request, **kwargs):
        pk = kwargs['pk']
        comment = Comment.objects.get(pk=pk)
        comment.delete()
        return redirect('blog_detail', comment.blog.slug)


class CategoryAddUser(View):
    def get(self, request, slug):
        category = Category.objects.get(slug=slug)
        user = CustomUser.objects.get(username=request.user.username)
        if user in category.user.all():
            category.user.remove(user)
            return redirect('categories')
        else:
            category.user.add(user)
            return redirect('categories')


class BlogUpdate(View):
    def get(self, request, slug):
        blog = Blog.objects.get(slug = slug)
        tags_value = ''
        for tag in blog.tags.all():
            tags_value += str(tag)
            tags_value += ','
        form = BlogUpdateForm(instance = blog)
        context = {
            'blog':blog,
            'form':form,
            'tags_value':tags_value
        }
        return render(request, 'blog/blog_update.html', context)
    def post(self, request, slug):
        blog = Blog.objects.get(slug = slug)
        form = BlogUpdateForm(request.POST, request.FILES, instance = blog)
        if form.is_valid():
            form_create = form.save(commit=False)
            form_create.slug = slugify(form_create.title)
            form_create.user = request.user
            form_create.save()
            tags = request.POST['xx'].split(',')
            for tag in blog.tags.all():
                if tag not in tags:
                    blog.tags.remove(tag)
            for tag in tags:
                if tag != '':
                    tag, created = Tag.objects.get_or_create(name = tag.strip())
                    blog.tags.add(tag)
            return redirect('home')