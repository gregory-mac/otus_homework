# Generated by Django 4.0.6 on 2022-07-10 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='biography',
            field=models.TextField(blank=True, max_length=300, null=True),
        ),
    ]