# Generated by Django 4.1.3 on 2023-01-10 06:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('littleLemon', '0004_person_person_age'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menu',
            old_name='cuisine',
            new_name='category',
        ),
    ]