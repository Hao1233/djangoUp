# Generated by Django 4.0.3 on 2022-04-07 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OurProfile', '0002_comment_customer_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
