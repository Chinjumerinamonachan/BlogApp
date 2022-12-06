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
    # def __str__(self):
    #     return self.article

class Comment(models.Model): 
    post = models.ForeignKey(Article,on_delete=models.CASCADE,related_name='comments')
    # name = models.CharField(max_length=80) 
    # email = models.EmailField()
    user=models.ForeignKey(USER, on_delete= models.CASCADE) 
    body = models.TextField() 
    created = models.DateTimeField(auto_now_add=True) 
    updated = models.DateTimeField(auto_now=True) 
    active = models.BooleanField(default=True) 

    class Meta: 
        ordering = ('created',) 

    def __str__(self): 
        return 'Comment by {} on {}'.format(self.user,self.post) 

class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    message=models.TextField()


    def __str__(self):
        return self.name
