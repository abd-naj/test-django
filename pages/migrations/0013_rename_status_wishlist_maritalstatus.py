# Generated by Django 4.1 on 2022-08-15 09:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("pages", "0012_rename_maritalstatus_wishlist_status"),
    ]

    operations = [
        migrations.RenameField(
            model_name="wishlist", old_name="status", new_name="maritalstatus",
        ),
    ]
