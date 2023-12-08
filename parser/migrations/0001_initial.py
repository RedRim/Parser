# Generated by Django 4.2.7 on 2023-12-06 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Имя')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('price', models.IntegerField(verbose_name='Цена')),
                ('link', models.CharField(max_length=400, verbose_name='Ссылка')),
                ('photo', models.ImageField(blank=True, upload_to='photos', verbose_name='Фото')),
            ],
            options={
                'indexes': [models.Index(fields=['slug'], name='parser_card_slug_94bd1c_idx')],
            },
        ),
    ]