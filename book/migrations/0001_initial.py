# Generated by Django 2.2 on 2019-08-18 17:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('born', models.DateTimeField()),
                ('died', models.DateTimeField(blank=True, null=True)),
                ('image', models.ImageField(upload_to=None)),
            ],
            options={
                'verbose_name': 'Author',
                'verbose_name_plural': 'Authors',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50)),
                ('amount', models.PositiveIntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('available', models.BooleanField(default=True)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to=None)),
                ('author', models.ManyToManyField(related_name='books', to='book.Author')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='books', to='book.Category')),
            ],
            options={
                'verbose_name': 'Book',
                'verbose_name_plural': 'Books',
            },
        ),
    ]
