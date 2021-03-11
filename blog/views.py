from django.shortcuts import render
from .models import Post
from django.views.generic import ListView

# CVB

# ListView의 경우 모델_list.html이라는 템플릿에 자동으로 연결됨
# 따라서 템플릿 네임을 따로 지정해주거나, 장고에 맞춰 post_list.html을 만들면 됨
class PostList(ListView):
    model = Post
    ordering = '-pk'


# FVB

# def index(request):
#     posts = Post.objects.all().order_by('-pk')
#
#     return render(
#         request,
#         'blog/post_list.html',
#         {
#             'posts':posts,
#         }
#     )
#
def single_post_page(request, pk):
    post = Post.objects.get(pk=pk)

    return render(
        request,
        'blog/single_post_page.html',
        {
            'post': post,
        }
    )