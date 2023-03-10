# Generated by Django 4.1.5 on 2023-01-17 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('FOREX', 'FOREX'), ('STOCK', 'STOCK'), ('CRYPTO', 'CRYPTO'), ('FUTURES', 'FUTURES'), ('OPTIONS', 'OPTIONS')], max_length=32)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.RemoveField(
            model_name='trade',
            name='market',
        ),
    ]
