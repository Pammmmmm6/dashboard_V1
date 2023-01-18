# Generated by Django 4.1.5 on 2023-01-18 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0003_trade_category_alter_category_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trade',
            name='category',
            field=models.CharField(choices=[('FOREX', 'FOREX'), ('STOCK', 'STOCK'), ('CRYPTO', 'CRYPTO'), ('FUTURES', 'FUTURES'), ('OPTIONS', 'OPTIONS')], default='CRYPTO', max_length=32),
        ),
    ]