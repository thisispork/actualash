from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from blog.models import Post, Author
from . import views


urlpatterns = [
url(r'^$',ListView.as_view(queryset = Post.objects.all().order_by("-date")[:25], template_name = "blog/index.html"), name='home'),
url(r'(?P<pk>\d+)$',DetailView.as_view(model=Post, template_name="blog/post.html")),
url('index/',DetailView.as_view(template_name="blog/index.html")),
url('about/',views.about, name='about'),
url('contact/', views.contact, name='contact'),
]
