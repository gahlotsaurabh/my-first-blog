# Generated by Django 2.1.5 on 2019-01-11 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='textss',
            field=models.TextField(default=True),
            preserve_default=False,
        ),
    ]
