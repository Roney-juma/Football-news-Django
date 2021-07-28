# Generated by Django 3.2.5 on 2021-07-28 21:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=200)),
                ('author', models.TextField(max_length=200, verbose_name='Author')),
                ('publishedAt', models.DateTimeField(verbose_name='Date Published')),
                ('description', models.TextField()),
                ('hero_image', models.TextField(verbose_name='Hero Image')),
                ('additional_image', models.TextField(blank=True, null=True, verbose_name='Additonal Image')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='football.category')),
            ],
        ),
    ]