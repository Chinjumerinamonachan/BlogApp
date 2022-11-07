from django.shortcuts import render,get_object_or_404,redirect
from myblog.models import Article,Like,Comment
from myblog.forms import ArticleForm,CommentForm

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

    comments = articles.comments.filter(active=True)

    new_comment = None

    if request.method == 'POST':
        # A comment was posted
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet          
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = articles
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()  
    
   
    template_name="myblog/detail.html"
    context={
        "articles":articles,
       'comments': comments,
    'new_comment': new_comment,
    'comment_form': comment_form
    
    }
    return render(request,template_name,context)

def like_post(request):
   
    user = USER.objects.get(username=request.user.username)
   
    print("...............",user)
    if request.method=='POST':
        article_id=request.POST.get('article_id')
        print("idddddddd.....",article_id)
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

    # return redirect('myblog:detail', kwargs={'article_id': article_id})
    return redirect('myblog:list')




def create_view(request):
    context ={}
    form = ArticleForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('myblog:home')
          
    context['form']= form
    return render(request, "myblog/create.html", context)





