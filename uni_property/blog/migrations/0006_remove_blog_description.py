# Generated by Django 4.0.5 on 2023-03-01 12:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_blog_other_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='description',
        ),
    ]
