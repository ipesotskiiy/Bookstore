# Generated by Django 4.1.4 on 2022-12-15 14:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=10, verbose_name='User role')),
                ('email', models.EmailField(db_index=True, max_length=40, verbose_name='Your email')),
                ('name', models.CharField(max_length=30, verbose_name='Your name')),
                ('password', models.CharField(max_length=255, verbose_name='Your password')),
                ('avatar', models.ImageField(blank=True, default='images/anonim_user.jpg', null=True, upload_to='', verbose_name='avatar')),
                ('comments', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.comment')),
                ('favorites', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.book')),
                ('ratings', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.rating')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
        ),
    ]
