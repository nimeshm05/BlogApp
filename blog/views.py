from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from django.db import connection
from django.contrib.auth.models import User
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


def home(request):
    context = {
        'posts': Post.objects.all()
        # Post.object.raw('SELECT * FROM blog_post')
    }
    return render(request, 'blog/home.html', context)


def dictfetchall(cursor):
    # Return all rows from a cursor as a dict
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


def common(request):
    cursor1 = connection.cursor()
    cursor1.execute("select auth_user.username, auth_user.email, users_profile.location from "
                    "auth_user, users_profile where users_profile.user_id = auth_user.id order by "
                    "auth_user.id")
    # cursor2.execute("select auth_user.username, blog_post.title, blog_post.date_posted from auth_user inner join "
    #                "blog_post "
    #                "on auth_user.id = blog_post.author_id")
    # cursor.execute("select username, date_joined, email from auth_user union select title, date_posted, author_id "
    #        "from blog_post order by date_joined")
    # cursor.execute("select username, title from auth_user, blog_post where blog_post.id = auth_user.id")
    # cursor.execute("select content from blog_post limit 3")
    row = dictfetchall(cursor1)
    return render(request, 'blog/common.html', {'data': row})

def titles(request):
    cursor2 = connection.cursor()
    cursor2.execute("select auth_user.username, blog_post.title, blog_post.category, blog_post.date_posted from "
                    "auth_user inner join "
                    "blog_post "
                    "on auth_user.id = blog_post.author_id")
    row2 = dictfetchall(cursor2)
    return render(request, 'blog/titles.html', {'data2': row2})

def favourite_book(request):
    cursor3 = connection.cursor()
    cursor3.execute("select blog_post.category, polls_poll.question from blog_post left join polls_poll"
                    "on polls_poll.username_id = blog_post.author_id")
    # cursor3.execute("select username, title, CASE WHEN count(title) = 2 THEN 'The user is a spammer' ELSE 'The user "
                   # "is not a spammer' END AS QuantityText FROM auth_user, blog_post")
    row3 = dictfetchall(cursor3)
    # row3 = Post.objects.all().values_list('favourite').union(User.objects.all().values_list('username'))
    return render(request, 'blog/user_fav.html', {'data3': row3})

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')
        # "select * from blog_post, auth_user where author_id = auth_user.id order by 'data_posted'"


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'category', 'favourite']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content', 'category', 'favourite']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
