# Generated by Django 3.1.7 on 2021-05-24 02:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_blogpost'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BlogPost',
        ),
    ]
