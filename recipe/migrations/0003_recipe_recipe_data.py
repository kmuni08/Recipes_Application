# Generated by Django 3.1.4 on 2021-07-29 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0002_recipe_users_wishlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='recipe_data',
            field=models.JSONField(default=dict),
        ),
    ]
