# Generated by Django 4.1.5 on 2023-01-18 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0002_category_remove_trade_market'),
    ]

    operations = [
        migrations.AddField(
            model_name='trade',
            name='category',
            field=models.CharField(choices=[('FOREX', 'FOREX'), ('STOCK', 'STOCK'), ('CRYPTO', 'CRYPTO'), ('FUTURES', 'FUTURES'), ('OPTIONS', 'OPTIONS')], default='', max_length=32),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=32),
        ),
    ]