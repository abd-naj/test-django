# Generated by Django 4.1 on 2022-08-15 09:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("pages", "0013_rename_status_wishlist_maritalstatus"),
    ]

    operations = [
        migrations.RenameField(
            model_name="wishlist", old_name="maritalstatus", new_name="status",
        ),
    ]