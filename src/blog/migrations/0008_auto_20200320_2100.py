# Generated by Django 3.0 on 2020-03-21 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_blogpostcomment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpostcomment',
            name='content',
            field=models.CharField(max_length=220),
        ),
    ]