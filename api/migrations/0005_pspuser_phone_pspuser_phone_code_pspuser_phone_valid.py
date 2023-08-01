# Generated by Django 4.1 on 2023-08-01 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_comment_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='pspuser',
            name='phone',
            field=models.CharField(blank=True, max_length=18, null=True),
        ),
        migrations.AddField(
            model_name='pspuser',
            name='phone_code',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pspuser',
            name='phone_valid',
            field=models.BooleanField(default=False),
        ),
    ]
