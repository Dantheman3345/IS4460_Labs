from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import render

from blog.models import Post
# Create your views here.

def get_posts(request):
    posts = Post.objects.all()
    context = {'posts':posts}
    return render(request,'blog/post_list.html',context)

def like_post(request,post_id):
    post = Post.objects.get(pk=post_id)
    post.likes += 1
    post.save()
    data = {'likes': post.likes, 'id':post_id}
    return JsonResponse(data)

