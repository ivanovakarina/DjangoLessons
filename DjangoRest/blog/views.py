from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Post
from django.http import JsonResponse

# Create your views here.
def posts(request):
    _posts = Post.objects.all() #список всех строк из Post
    return render(request, 'blog/posts.html', {'posts': _posts}) #запрос,шаблон, словарь с переменными

def post(request, post_id):
    _post = Post.object.get(pk=post_id)
    #_post = get_object_or_404(Post, pk=post_id)
    return render(request, 'blog/post.html', {'post': _post})

def login_view(request):
    return HttpResponse('')

#def api_post(request):
#    if request.method == 'GET':
#        response = {
#            'title' : request.GET.get('title'),
#            'text' : request.GET.get('text'),
#            'date': '2017-02-03'
#        }
#    else:
#        response = {'q': 1, 'w': 2}
#    return HttpResponse(title)
def api_posts(request):
    _posts = []
    all_posts = Post.objects.all()
    for post in all_posts:
        _posts.append({
            'id': post.id,
            'title': post.title,
            'text': post.text,
            'image': 'http://127.0.0.1:8000/blog/media/' + str(post.image)
        })

    return JsonResponse({'posts': _posts})

def api_post(request):
    post_id = request.GET.get('id')
    post = Post.objects.get(pk = post_id)
    if request.method == 'GET':
        response = {
            'id': post.id,
            'title': post.title,
            'text': post.text,

        }
    return JsonResponse(response)