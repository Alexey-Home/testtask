# Generated by Django 3.1.14 on 2023-09-20 12:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lessons',
            name='products',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='API.products', verbose_name='Продукт'),
        ),
    ]
