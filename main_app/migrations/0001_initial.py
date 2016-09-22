# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-21 15:44
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
                ('Basics', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Formation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
                ('Description', models.TextField()),
                ('Pre_basics', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
                ('Location', models.CharField(max_length=200)),
                ('Type', models.CharField(max_length=200)),
                ('Basics', models.TextField()),
                ('Rating', models.DecimalField(decimal_places=2, max_digits=4)),
                ('Website', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=200)),
                ('Country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Country')),
            ],
        ),
        migrations.AddField(
            model_name='formation',
            name='School',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.School'),
        ),
    ]