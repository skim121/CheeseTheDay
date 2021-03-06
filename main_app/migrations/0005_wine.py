# Generated by Django 4.0.3 on 2022-03-28 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_cheese_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('type', models.CharField(choices=[('red', 'red'), ('white', 'white'), ('rose', 'rose'), ('sparkling', 'sparkling')], max_length=20)),
                ('sweetness', models.CharField(choices=[('dry', 'dry'), ('medium', 'medium'), ('sweet', 'sweet')], max_length=100)),
            ],
        ),
    ]
