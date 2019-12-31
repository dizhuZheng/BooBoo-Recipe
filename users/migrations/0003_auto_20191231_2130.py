# Generated by Django 3.0.1 on 2019-12-31 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_userprofile_gender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='mobile',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='nick_name',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='job',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Job'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='address',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Address'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='email',
            field=models.EmailField(blank=True, max_length=150, null=True, verbose_name='Email'),
        ),
    ]