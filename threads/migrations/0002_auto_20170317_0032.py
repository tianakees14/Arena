# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2017-03-16 19:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('threads', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Followers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=100, verbose_name='User Name')),
                ('follower', models.CharField(max_length=100, verbose_name='User Name')),
            ],
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=100, verbose_name='Question')),
                ('user_name', models.CharField(max_length=100, verbose_name='User Name')),
                ('posted', models.DateTimeField(auto_now_add=True)),
                ('domain', models.CharField(max_length=100, verbose_name='Domain')),
            ],
            options={
                'verbose_name_plural': 'Questions',
                'verbose_name': 'Questions',
            },
        ),
        migrations.CreateModel(
            name='Replies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_id', models.IntegerField()),
                ('posted', models.DateTimeField(auto_now_add=True)),
                ('rank', models.IntegerField()),
                ('reply', models.CharField(max_length=100, verbose_name='Reply')),
                ('votes', models.IntegerField()),
                ('domain', models.CharField(max_length=100, verbose_name='Domain')),
            ],
            options={
                'verbose_name_plural': 'Replies',
                'verbose_name': 'Replies',
            },
        ),
        migrations.CreateModel(
            name='Requests',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=100, verbose_name='User Name')),
                ('requestor', models.CharField(max_length=100, verbose_name='User Name')),
            ],
        ),
        migrations.CreateModel(
            name='ThreadReplies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reply_id', models.IntegerField()),
                ('reply', models.CharField(max_length=100, verbose_name='Reply')),
                ('votes', models.IntegerField()),
                ('rank', models.IntegerField()),
                ('posted', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Thread Replies',
                'verbose_name': 'Thread Replies',
            },
        ),
        migrations.AddField(
            model_name='profile',
            name='score',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='email_id',
            field=models.EmailField(max_length=254),
        ),
    ]
