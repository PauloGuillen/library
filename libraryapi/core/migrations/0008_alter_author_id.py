# Generated by Django 4.2.4 on 2023-08-15 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_author_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='id',
            field=models.BigIntegerField(default=207145654879554, editable=False, primary_key=True, serialize=False),
        ),
    ]
