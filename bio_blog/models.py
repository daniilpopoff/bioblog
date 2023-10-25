from django.db import models
from django.conf import settings
from django.utils import timezone
from ckeditor.fields import RichTextField

# Create your models here.

class Post(models.Model):
    TYPE_POST = (
        ('computer Sciense', 'COMPUTER SCIENSE'),
        ('bioinformatics', 'BIOINFORMATICS'),
        ('data sciense', 'DATA SCIENSE'),


    )

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    preview_img = models.ImageField(upload_to='uploads/post_prewiew')
    text = RichTextField()
    type_post = models.CharField(max_length=20, choices=TYPE_POST, default=TYPE_POST[0][0] )
    created_at = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True)



    def publich(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
