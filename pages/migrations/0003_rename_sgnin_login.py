# Generated by Django 4.1 on 2022-08-13 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("pages", "0002_rename_login_sgnin"),
    ]

    operations = [
        migrations.RenameModel(old_name="sgnin", new_name="Login",),
    ]
