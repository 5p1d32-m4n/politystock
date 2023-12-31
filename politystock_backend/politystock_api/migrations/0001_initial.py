# Generated by Django 4.2.4 on 2023-08-28 00:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Politician',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('party', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('district', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(max_length=255)),
                ('company', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_date', models.DateField()),
                ('transaction_type', models.CharField(choices=[('Buy', 'Buy'), ('Sell', 'Sell'), ('Dividend', 'Dividend')], max_length=255)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('politician', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='politystock_api.politician')),
                ('stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='politystock_api.stock')),
            ],
        ),
    ]
