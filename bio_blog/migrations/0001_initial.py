# Generated by Django 4.2.6 on 2023-10-30 13:57

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='HeartDiseaseData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.FloatField()),
                ('sex', models.FloatField()),
                ('cp', models.FloatField()),
                ('trestbps', models.FloatField()),
                ('chol', models.FloatField()),
                ('fbs', models.FloatField()),
                ('restecg', models.FloatField()),
                ('thalach', models.FloatField()),
                ('exang', models.FloatField()),
                ('oldpeak', models.FloatField()),
                ('slope', models.FloatField()),
                ('ca', models.FloatField()),
                ('thal', models.FloatField()),
                ('predicted_value', models.BooleanField(blank=True, default=None, null=True)),
                ('submited_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('preview_img', models.ImageField(upload_to='uploads/post_prewiew')),
                ('text', ckeditor.fields.RichTextField()),
                ('type_post', models.CharField(choices=[('computer Sciense', 'COMPUTER SCIENSE'), ('bioinformatics', 'BIOINFORMATICS'), ('data sciense', 'DATA SCIENSE')], default='computer Sciense', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
