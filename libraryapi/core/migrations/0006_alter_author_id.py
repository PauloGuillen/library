# Generated by Django 4.2.4 on 2023-08-15 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_author_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='id',
            field=models.IntegerField(default=70276808279695, editable=False, primary_key=True, serialize=False),
        ),
    ]
