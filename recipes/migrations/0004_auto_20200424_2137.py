# Generated by Django 3.0.1 on 2020-04-24 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='text',
        ),
        migrations.AddField(
            model_name='image',
            name='name',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
