# Generated by Django 4.1.5 on 2023-02-20 04:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Consultorias', '0010_mentor_mentor_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mentor',
            name='mentor_image',
        ),
    ]
