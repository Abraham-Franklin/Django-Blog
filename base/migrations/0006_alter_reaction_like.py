# Generated by Django 4.1.7 on 2023-06-01 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_reaction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reaction',
            name='like',
            field=models.BooleanField(default=False),
        ),
    ]
