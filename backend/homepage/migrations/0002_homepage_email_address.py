# Generated by Django 4.2.1 on 2023-05-31 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='email_address',
            field=models.EmailField(default='none', max_length=120),
            preserve_default=False,
        ),
    ]
