# Generated by Django 4.0.2 on 2022-02-13 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0007_alter_blog_update_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='author',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='blog',
            name='date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='blog',
            name='genre',
            field=models.CharField(blank=True, choices=[('Science and Technology', 'Science and Technology'), ('Literature', 'Literature'), ('Action', 'Action'), ('Personal Expierence', 'Personal Expierence')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
