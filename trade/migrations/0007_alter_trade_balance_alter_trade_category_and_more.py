# Generated by Django 4.1.5 on 2023-01-18 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0006_alter_trade_balance_alter_trade_profit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trade',
            name='balance',
            field=models.DecimalField(decimal_places=2, max_digits=16),
        ),
        migrations.AlterField(
            model_name='trade',
            name='category',
            field=models.CharField(choices=[('FOREX', 'FOREX'), ('STOCK', 'STOCK'), ('CRYPTO', 'CRYPTO'), ('FUTURES', 'FUTURES'), ('OPTIONS', 'OPTIONS'), ('NONE', 'NONE')], default='NONE', max_length=32),
        ),
        migrations.AlterField(
            model_name='trade',
            name='profit',
            field=models.DecimalField(decimal_places=2, max_digits=16),
        ),
    ]