# Generated by Django 3.2.16 on 2023-05-12 13:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_alter_follow_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='follow',
            old_name='author',
            new_name='following',
        ),
    ]