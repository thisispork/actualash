# Generated by Django 2.1 on 2018-09-19 01:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_celebrity_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='blog/pics/'),
            preserve_default=False,
        ),
    ]