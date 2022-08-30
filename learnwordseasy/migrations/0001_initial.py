# Generated by Django 4.1 on 2022-08-30 13:13

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
                ('title1', models.CharField(db_index=True, max_length=150, verbose_name='Наименование категории')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ['title1'],
            },
        ),
        migrations.CreateModel(
            name='Words',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title1', models.CharField(max_length=150, verbose_name='Слово')),
                ('title2', models.CharField(max_length=150, null=True, verbose_name='Перевод')),
                ('example1', models.TextField(blank=True, verbose_name='Предлложение 1')),
                ('example2', models.TextField(blank=True, verbose_name='Предлложение 2')),
                ('example3', models.TextField(blank=True, verbose_name='Предлложение 3')),
                ('photo', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/', verbose_name='Фото')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='learnwordseasy.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Слово',
                'verbose_name_plural': 'Слова',
                'ordering': ['-created_at'],
            },
        ),
    ]