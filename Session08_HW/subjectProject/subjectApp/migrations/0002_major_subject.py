# Generated by Django 4.0.3 on 2022-04-07 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subjectApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='major',
            name='subject',
            field=models.TextField(default='', null=True),
        ),
    ]
