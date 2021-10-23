# Generated by Django 3.2 on 2021-05-19 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stock_Information',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock_code', models.DecimalField(decimal_places=0, max_digits=5)),
                ('stock_name', models.CharField(max_length=20)),
                ('stock_year', models.DecimalField(decimal_places=0, max_digits=5)),
                ('stock_month', models.DecimalField(decimal_places=0, max_digits=2)),
                ('stock_day', models.DecimalField(decimal_places=0, max_digits=3)),
                ('stock_capacity', models.DecimalField(decimal_places=0, max_digits=50)),
                ('stock_turnover', models.DecimalField(decimal_places=0, max_digits=50)),
                ('stock_open', models.DecimalField(decimal_places=1, max_digits=20)),
                ('stock_high', models.DecimalField(decimal_places=1, max_digits=20)),
                ('stock_low', models.DecimalField(decimal_places=1, max_digits=20)),
                ('stock_close', models.DecimalField(decimal_places=1, max_digits=20)),
                ('stock_change', models.SmallIntegerField()),
                ('stock_transaction', models.DecimalField(decimal_places=0, max_digits=50)),
            ],
        ),
    ]