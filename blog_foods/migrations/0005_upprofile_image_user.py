# Generated by Django 3.2.9 on 2021-11-03 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_foods', '0004_auto_20211103_1724'),
    ]

    operations = [
        migrations.AddField(
            model_name='upprofile',
            name='image_user',
            field=models.ImageField(default='blank-profile-picture.png', upload_to='image_user'),
        ),
    ]
