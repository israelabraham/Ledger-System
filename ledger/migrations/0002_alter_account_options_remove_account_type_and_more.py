# Generated by Django 4.0.5 on 2022-06-07 22:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ledger', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='account',
            options={'verbose_name_plural': 'User Accounts'},
        ),
        migrations.RemoveField(
            model_name='account',
            name='type',
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(help_text='account name to deposit', max_length=255, unique=True)),
                ('slug', models.SlugField(null=True)),
                ('amount', models.FloatField(default=0.0)),
                ('type', models.CharField(choices=[('deposit', 'desposit'), ('withdraw', 'withdraw'), ('transfer', 'transfer')], max_length=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ledger.user')),
            ],
            options={
                'verbose_name_plural': 'User Transactions',
                'db_table': 'transactions',
            },
        ),
    ]
