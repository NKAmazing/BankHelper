# Generated by Django 3.2.12 on 2023-07-03 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0006_auto_20230703_0030'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
    ]