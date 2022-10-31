from django.shortcuts import render,get_object_or_404,redirect
from myblog.models import Article
from myblog.forms import ArticleForm
from django.contrib.auth import get_user_model

USER = get_user_model()

def home_view(request):
    template_name="myblog/index.html"
    return render(request,template_name)

def list_view(request):
    # current_user=request.USER
    # print("userrrrrrr: ",current_user)
    # articles=Article.objects.filter(status=1,author=current_user).order_by('-created_on')
    articles=Article.objects.filter(status=1).order_by('-created_on')
    # template_name="myblog/index.html"
    template_name="myblog/list.html"
    context={"articles":articles}
    return render(request,template_name,context)

def detail_view(request,aid):
    print("haiiiiiiiiii")
    articles=get_object_or_404(Article,pk=aid)
   
    template_name="myblog/detail.html"
    context={"articles":articles}
    return render(request,template_name,context)

def create_view(request):
    context ={}
    form = ArticleForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('myblog:home')
          
    context['form']= form
    return render(request, "myblog/create.html", context)

