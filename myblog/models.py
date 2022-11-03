from django.db import models
from django.contrib.auth import get_user_model

USER = get_user_model()

# Create your models here.
STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Article(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    author = models.ForeignKey(USER, on_delete= models.CASCADE,related_name='blog_posts')
    image = models.ImageField(upload_to="myblog/image", default="default/blog.png")
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(USER, related_name='likes',blank=True,default=None)

   

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
    @property
    def num_likes(self):
        return self.likes.all().count()

Like_Choices=(
    ('Like','Like'),
    ('Unlike','Unlike')
)

class Like(models.Model):
    user=models.ForeignKey(USER, on_delete= models.CASCADE)
    article=models.ForeignKey(Article, on_delete= models.CASCADE)
    value=models.CharField(choices=Like_Choices,default='Like',max_length=10)
def __str__(self):
    return self.article

class Comment(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    content = models.TextField()
    post = models.ForeignKey(Article, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return 'Comment by {}'.format(self.name)