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

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title