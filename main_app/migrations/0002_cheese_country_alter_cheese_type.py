# Generated by Django 4.0.3 on 2022-03-26 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cheese',
            name='country',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cheese',
            name='type',
            field=models.CharField(choices=[('f', 'fresh'), ('s', 'soft'), ('sf', 'semi-firm'), ('h', 'hard'), ('b', 'blue')], max_length=100),
        ),
    ]