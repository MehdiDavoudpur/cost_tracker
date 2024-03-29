# Generated by Django 5.0.2 on 2024-02-28 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CostEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('cost_for', models.CharField(max_length=100)),
                ('cost_group', models.CharField(choices=[('Food', 'Food'), ('Clothes', 'Clothes'), ('Housing', 'Housing'), ('Health', 'Health'), ('Education', 'Education'), ('Entertainment & Welfare', 'Entertainment & Welfare'), ('Transportation', 'Transportation')], max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
