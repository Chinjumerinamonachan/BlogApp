from django.shortcuts import render,get_object_or_404,redirect
from myblog.models import Article,Like
from myblog.forms import ArticleForm
from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect

USER = get_user_model()

def home_view(request):
    # user1 = USER.objects.all()
    # user = USER.objects.get('username')
    
    articles=Article.objects.filter(status=1).order_by('-created_on')
    context={"articles":articles
    # "user":user
    }
    template_name="myblog/index.html"
    return render(request,template_name,context)

def list_view(request):
    user = USER.objects.get(username=request.user.username)
    print("//////",user)
    articles=Article.objects.filter(status=1,author=user).order_by('-created_on')
    
    template_name="myblog/list.html"
    context={"articles":articles
    }
    return render(request,template_name,context)

def detail_view(request,aid):
    print("haiiiiiiiiii")
    articles=get_object_or_404(Article,pk=aid)
    
   
    template_name="myblog/detail.html"
    context={
        "articles":articles
       
    
    }
    return render(request,template_name,context)

def like_post(request):
    # user = request.user
    user = USER.objects.get(username=request.user.username)
    
    print("...............",user)
    if request.method=='POST':
        article_id=request.POST.get('article_id')
        aricle_obj=Article.objects.get(id=article_id)

        if user in aricle_obj.likes.all():
            aricle_obj.likes.remove(user)
        else:
            aricle_obj.likes.add(user)
    like,created=Like.objects.get_or_create(user=user,article_id=article_id)
    if not created:
        if like.value=='Like':
            like.value='UnLike'
        else:
            like.value='Like'
    like.save()

    return redirect('myblog:home')


def create_view(request):
    context ={}
    form = ArticleForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('myblog:home')
          
    context['form']= form
    return render(request, "myblog/create.html", context)





