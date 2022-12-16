# Generated by Django 4.1.4 on 2022-12-15 14:49

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Comment date')),
                ('text', models.TextField(max_length=900, verbose_name='Comment')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Genre')),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.FloatField(max_length=3, verbose_name='Rating')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Book title')),
                ('author', models.CharField(max_length=80, verbose_name='Author')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Price')),
                ('cover', models.CharField(blank=True, max_length=15, null=True, verbose_name='Cover')),
                ('date_of_issue', models.DateField(default=django.utils.timezone.now, verbose_name='Date of Issue')),
                ('in_stock', models.PositiveIntegerField(blank=True, null=True, verbose_name='In stock')),
                ('description', models.TextField(blank=True, max_length=900, null=True, verbose_name='Description')),
                ('average_rate', models.FloatField(blank=True, max_length=3, null=True, verbose_name='Average rate')),
                ('is_in_favorite', models.BooleanField()),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.comment')),
                ('genre', models.ManyToManyField(to='product.genre')),
                ('rating', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.rating')),
            ],
            options={
                'verbose_name': 'Book',
                'verbose_name_plural': 'Books',
            },
        ),
    ]
