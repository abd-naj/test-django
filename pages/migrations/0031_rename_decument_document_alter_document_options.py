# Generated by Django 4.1 on 2022-08-18 13:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("pages", "0030_decument"),
    ]

    operations = [
        migrations.RenameModel(old_name="Decument", new_name="Document",),
        migrations.AlterModelOptions(
            name="document", options={"verbose_name": "select document"},
        ),
    ]