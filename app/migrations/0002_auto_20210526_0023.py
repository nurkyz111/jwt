# Generated by Django 3.2.3 on 2021-05-25 18:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Quiz',
            new_name='App',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='quiz',
            new_name='app',
        ),
    ]