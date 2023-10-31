from django.db import models
from django.conf import settings
from django.utils import timezone
from ckeditor.fields import RichTextField
from accounts.models import CustomUser

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



    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class HeartDiseaseData(models.Model):
    age = models.FloatField()
    sex = models.FloatField()
    cp = models.FloatField()
    trestbps = models.FloatField()
    chol = models.FloatField()
    fbs = models.FloatField()
    restecg = models.FloatField()
    thalach = models.FloatField()
    exang = models.FloatField()
    oldpeak = models.FloatField()
    slope = models.FloatField()
    ca = models.FloatField()
    thal = models.FloatField()
    predicted_value = models.BooleanField(blank=True, null=True, default=None)
    submited_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    def submit(self):
        self.submited = timezone.now()
        self.save()
