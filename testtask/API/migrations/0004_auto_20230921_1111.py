# Generated by Django 3.1.14 on 2023-09-21 08:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('API', '0003_auto_20230921_0956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lessons',
            name='link',
            field=models.CharField(max_length=500, verbose_name='Ссылка на видео'),
        ),
        migrations.AlterField(
            model_name='lessons',
            name='title',
            field=models.CharField(db_index=True, max_length=500, verbose_name='Название'),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('products', models.ManyToManyField(to='API.Products', verbose_name='Продукт')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
